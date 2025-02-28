# coding: utf-8
from sqlalchemy import CheckConstraint, Column, Date, DateTime, Enum, ForeignKey, Integer, Numeric, String, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import TSRANGE
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()
metadata = Base.metadata


class Cliente(Base):
    __tablename__ = 'cliente'

    cliente_id = Column(Integer, primary_key=True, server_default=text("nextval('cliente_cliente_id_seq'::regclass)"))
    nombre = Column(String(255), nullable=False)
    direccion = Column(String(255))
    telefono = Column(String(50))
    email = Column(String(255), unique=True)


class Divisa(Base):
    __tablename__ = 'divisa'

    divisa_id = Column(Integer, primary_key=True, server_default=text("nextval('divisa_divisa_id_seq'::regclass)"))
    codigo = Column(Enum('USD', 'EUR', 'MXN', name='codigo_divisa'), nullable=False, unique=True)
    nombre = Column(String(50), nullable=False)


class Empleado(Base):
    __tablename__ = 'empleado'
    __table_args__ = (
        CheckConstraint('(jerarquia >= 1) AND (jerarquia <= 5)'),
    )

    empleado_id = Column(Integer, primary_key=True, server_default=text("nextval('empleado_empleado_id_seq'::regclass)"))
    nombre = Column(String(255), nullable=False)
    contacto = Column(String(255))
    jerarquia = Column(Integer, nullable=False)
    rol = Column(Enum('Mesero', 'Coordinador', 'Chef', 'Musico', name='rol_empleado'), nullable=False)


class Salon(Base):
    __tablename__ = 'salon'

    salon_id = Column(Integer, primary_key=True, server_default=text("nextval('salon_salon_id_seq'::regclass)"))
    nombre = Column(String(255), nullable=False)
    ubicacion = Column(String(255))
    capacidad = Column(Integer)


class Servicio(Base):
    __tablename__ = 'servicio'

    servicio_id = Column(Integer, primary_key=True, server_default=text("nextval('servicio_servicio_id_seq'::regclass)"))
    nombre = Column(Enum('Catering', 'Música en vivo', 'Decoración temática', name='tipo_servicio'), nullable=False)
    descripcion = Column(Text)


    costo_base = Column(Numeric(10, 2), nullable=False)


class TemporadaTarifa(Base):
    __tablename__ = 'temporada_tarifa'

    temporada_id = Column(Integer, primary_key=True, server_default=text("nextval('temporada_tarifa_temporada_id_seq'::regclass)"))
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    modificador_tarifa = Column(Numeric(5, 2), nullable=False)
    descripcion = Column(Text)


class Evento(Base):
    __tablename__ = 'evento'
    __table_args__ = (
        CheckConstraint("(categoria)::text = ANY (ARRAY[('conferencia'::character varying)::text, ('boda'::character varying)::text, ('reunion_corporativa'::character varying)::text, ('cena_privada'::character varying)::text])"),
    )

    evento_id = Column(Integer, primary_key=True, server_default=text("nextval('evento_evento_id_seq'::regclass)"))
    nombre = Column(String(255), nullable=False, index=True)
    descripcion = Column(Text, index=True)
    categoria = Column(Enum('Conferencia', 'Boda', 'Reunion Corporativa', 'Cena privada', name='categoria_evento'), nullable=False)
    fecha_programada = Column(DateTime)
    cliente_id = Column(ForeignKey('cliente.cliente_id'), nullable=False)

    cliente = relationship('Cliente')


class AsignacionEmpleadoEvento(Base):
    __tablename__ = 'asignacion_empleado_evento'
    __table_args__ = (
        CheckConstraint('hora_fin > hora_inicio'),
    )

    asignacion_id = Column(Integer, primary_key=True, server_default=text("nextval('asignacion_empleado_evento_asignacion_id_seq'::regclass)"))
    evento_id = Column(ForeignKey('evento.evento_id'), nullable=False)
    empleado_id = Column(ForeignKey('empleado.empleado_id'), nullable=False)
    hora_inicio = Column(DateTime, nullable=False)
    hora_fin = Column(DateTime, nullable=False)

    empleado = relationship('Empleado')
    evento = relationship('Evento')


class HistorialEvento(Base):
    __tablename__ = 'historial_evento'

    evento_historial_id = Column(Integer, primary_key=True, server_default=text("nextval('historial_evento_evento_historial_id_seq'::regclass)"))
    evento_id = Column(ForeignKey('evento.evento_id'), nullable=False)
    fecha_modificacion = Column(DateTime, nullable=False, server_default=text("now()"))
    nombre_modificado = Column(String(255))
    descripcion_modificada = Column(Text)
    modificado_por = Column(String(255))

    evento = relationship('Evento')


class Reservacion(Base):
    __tablename__ = 'reservacion'

    reservacion_id = Column(Integer, primary_key=True, server_default=text("nextval('reservacion_reservacion_id_seq'::regclass)"))
    evento_id = Column(ForeignKey('evento.evento_id'), nullable=False)
    cliente_id = Column(ForeignKey('cliente.cliente_id'))
    fecha_solicitud = Column(DateTime, nullable=False, server_default=text("now()"))
    fecha_evento = Column(DateTime, nullable=False)
    fecha_cancelacion = Column(DateTime)
    salon_id = Column(ForeignKey('salon.salon_id'), nullable=False)
    rango_horario = Column(TSRANGE, nullable=False)
    tarifa_aplicada = Column(Numeric(10, 2))

    cliente = relationship('Cliente')
    evento = relationship('Evento')
    salon = relationship('Salon')


class Factura(Base):
    __tablename__ = 'factura'

    factura_id = Column(Integer, primary_key=True, server_default=text("nextval('factura_factura_id_seq'::regclass)"))
    reservacion_id = Column(ForeignKey('reservacion.reservacion_id'), nullable=False)
    total = Column(Numeric(10, 2), nullable=False, server_default=text("0"))
    fecha_pago = Column(DateTime)
    moneda = Column(String(10), nullable=False)
    tasa_cambio = Column(Numeric(10, 4))
    descuento = Column(Numeric(10, 2), server_default=text("0"))
    penalizacion = Column(Numeric(10, 2), server_default=text("0"))
    monto_convertido = Column(Numeric(10, 2))

    reservacion = relationship('Reservacion')


class ReservacionServicio(Base):
    __tablename__ = 'reservacion_servicio'

    reservacion_id = Column(ForeignKey('reservacion.reservacion_id'), primary_key=True, nullable=False)
    servicio_id = Column(ForeignKey('servicio.servicio_id'), primary_key=True, nullable=False)
    cantidad = Column(Integer, server_default=text("1"))
    costo_aplicado = Column(Numeric(10, 2), nullable=False)

    reservacion = relationship('Reservacion')
    servicio = relationship('Servicio')


class TransaccionDivisa(Base):
    __tablename__ = 'transaccion_divisa'
    __table_args__ = (
        CheckConstraint("(tipo_transaccion)::text = ANY ((ARRAY['compra'::character varying, 'venta'::character varying])::text[])"),
    )

    transaccion_id = Column(Integer, primary_key=True, server_default=text("nextval('transaccion_divisa_transaccion_id_seq'::regclass)"))
    factura_id = Column(ForeignKey('factura.factura_id'), nullable=False)
    fecha_transaccion = Column(DateTime, nullable=False, server_default=text("now()"))
    tipo_transaccion = Column(String(20), nullable=False)
    moneda_origen = Column(String(10), nullable=False)
    moneda_destino = Column(String(10), nullable=False)
    tasa_aplicada = Column(Numeric(10, 4), nullable=False)

    factura = relationship('Factura')
