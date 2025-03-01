from models import Evento, Cliente, Empleado, Factura, HistorialEvento, AsignacionEmpleadoEvento, Salon, Servicio, Divisa, TemporadaTarifa, ReservacionServicio, Servicio, Reservacion
from sqlalchemy import create_engine, and_, or_, func, extract, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import NoResultFound
from datetime import datetime


#Change database connection data
DATABASE_URL =  "postgresql://postgres:Platano45@localhost/Hoteleria_oficial"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


#List
def get_currency():
    divisas = session.query(Divisa).all()
    for divisa in divisas:
        print(divisa.divisa_id, divisa.codigo, divisa.nombre)

def get_season_currency():
    season_currency = session.query(TemporadaTarifa).all()
    for s_currency in season_currency:
        print(s_currency.temporada_id, s_currency.fecha_inicio, s_currency.fecha_fin, s_currency.modificador_tarifa, s_currency.descripcion)

def get_service_reservation():
    services = session.query(ReservacionServicio).all()
    for service in services:
        print(service.reservacion_id, service.servicio_id, service.cantidad, service.costo_aplicado)

def get_service():
    services = session.query(Servicio).all()
    for service in services:
        print(service.servicio_id, service.nombre, service.descripcion)


def get_hall():
    halls = session.query(Salon).all()
    for hall in halls:
        print(hall.salon_id, hall.nombre, hall.ubicacion, hall.capacidad)

#insert
def insert_event(evento_id, nombre, descripcion, categoria, fecha_programada, cliente_id):
    event = Evento(evento_id, nombre, descripcion, categoria, fecha_programada, cliente_id)
    session.add(event)
    session.commit()

def insert_client(cliente_id, nombre, direccion, telefono, email):
    client = Cliente(cliente_id, nombre, direccion, telefono, email)
    session.add(client)
    session.commit()

def insert_employee(empleado_id, nombre,contacto, jerarquia, rol):
    employee = Empleado(empleado_id, nombre, contacto, jerarquia, rol)
    session.add(employee)
    session.commit()

def insert_hall(salon_id, nombre, ubicacion, capacidad):
    hall = Salon(salon_id, nombre, ubicacion, capacidad)
    session.add(hall)
    session.commit()

def insert_service(servicio_id, nombre, descripcion, costo_base):
    service  = Servicio(servicio_id, nombre, descripcion, costo_base)
    session.add(service)
    session.commit()
#delete

def delete_client(id):
    client = session.get(Cliente, int(id))
    if client:
        session.delete(client)
        session.commit()
        print("cliente eliminado correctamente")
    else:
         print("El cliente no se ha contrado")

def delete_currency(id):
    currency = session.get(Divisa, int(id))
    if currency:
        session.delete(currency)
        session.commit()
        print("Divisa eliminado correctamente")
    else:
         print("La divisa no se ha contrado")

def delete_employee(id):
    empleado = session.get(Empleado, int(id))
    if empleado:
        session.delete(empleado)
        session.commit()
        print("Empleado eliminado correctamente")
    else:
         print("El Empleado no se ha contrado")

def delete_hall(id):
    hall = session.get(Salon, int(id))
    if hall:
        session.delete(hall)
        session.commit()
        print("Salon eliminado correctamente")
    else:
         print("El salonno se ha contrado")

def delete_service():
    service = session.get(Servicio, int(id))
    if service:
        session.delete(service)
        session.commit()
        print("Servicio eliminado correctamente")
    else:
         print("El servicio se ha contrado")


#update

def update_service(id, description):
    service = session.get(Servicio, int(id))
    if service:
        service.descripcion = description
        session.commit()
        print("Servicio actualizado correctamente")
    else:
        print("Servicio no encontrado")

def update_client(id, phone):
    client = session.get(Cliente, int(id))
    if client:
        client.telefono = phone
        session.commit()
        print("Cliente actualizado correctamente")
    else:
        print("Cliente no encontrado")

def update_employee(id, contacto):
    employee = session.get(Empleado, int(id))
    if employee:
        employee.contacto = contacto
        session.commit()
        print("Empleado actualizado correctamente")
    else:
        print("Empleado no encontrado")

def update_hall(id, ubicacion):
    hall = session.get(Salon, int(id))
    if hall:
        hall.ubicacion = ubicacion
        session.commit()
        print("Salon actualizado correctamente")
    else:
        print("Salon no encontrado")

def update_event(id, description):
    event = session.get(Evento, int(id))
    if event:
        event.descripcion = description
        session.commit()
        print("Evento actualizado correctamente")
    else:
        print("Evento no encontrado")

#getbyid
def get_event_byid(evento_id):
    try:
        evento = session.query(Evento).get(evento_id)
        print(evento.evento_id, evento.nombre, evento.descripcion, evento.categoria, evento.fecha_programada, evento.cliente_id)
    except NoResultFound:
        return None

def get_currency_byid(divisa_id):
    try:
        divisa = session.query(Divisa).get(divisa_id)
        print(divisa.divisa_id, divisa.codigo, divisa.nombre)
    except NoResultFound:
        return None
    
def get_hall_byid(salon_id):
    try:
        salon = session.query(Salon).get(salon_id)
        print(salon.salon_id, salon.nombre, salon.ubicacion, salon.capacidad)
    except NoResultFound:
        return None

def get_service_byid(servicio_id):
    try:
        servicio = session.query(Servicio).get(servicio_id)
        print(servicio.servicio_id, servicio.nombre, servicio.descripcion)
    except NoResultFound:
        return None
    
def get_employee_byid(empleado_id):
    try:
        empleado = session.query(Empleado).get(empleado_id)
        print(empleado.empleado_id, empleado.nombre, empleado.contacto, empleado.jerarquia, empleado.rol)
    except NoResultFound:
        return None
    
#Desglozar eventos por mes y año 
def informe_ingresos_por_mes(mes, año):
    ingresos = session.query(
        Evento.categoria,
        func.sum(Factura.total).label('ingresos_totales')
    ).join(Reservacion, Evento.evento_id == Reservacion.evento_id)\
     .join(Factura, Reservacion.reservacion_id == Factura.reservacion_id)\
     .filter(
         and_(
             extract('month', Reservacion.fecha_evento) == mes,
             extract('year', Reservacion.fecha_evento) == año
         )
     ).group_by(Evento.categoria).all()

    for categoria, ingresos_totales in ingresos:
        print(f"Categoría: {categoria}, Ingresos Totales: {ingresos_totales}")
#Listar eventos por fecha        
def listar_eventos_por_fecha(fecha):
    try:
        if not isinstance(fecha, str):
            raise ValueError("La fecha debe ser una cadena en formato 'YYYY-MM-DD'.")

        fecha_deseada = datetime.strptime(fecha, '%Y-%m-%d').date()

        eventos = session.query(
            Evento.nombre.label('nombre_evento'),
            Evento.categoria.label('tipo_evento'),
            Salon.ubicacion.label('ubicacion_evento'),
            Cliente.nombre.label('nombre_cliente'),
            Cliente.email.label('email_cliente')
        ).join(
            Cliente, Evento.cliente_id == Cliente.cliente_id
        ).join(
            Reservacion, Evento.evento_id == Reservacion.evento_id
        ).join(
            Salon, Reservacion.salon_id == Salon.salon_id
        ).filter(
            func.date(Reservacion.fecha_evento) == fecha_deseada
        ).all()

        if eventos:
            print(f"Eventos programados para el {fecha}:")
            for evento in eventos:
                print(f"Nombre: {evento.nombre_evento}, Tipo: {evento.tipo_evento}, "
                      f"Ubicación: {evento.ubicacion_evento}, Cliente: {evento.nombre_cliente}, "
                      f"Email: {evento.email_cliente}")
        else:
            print(f"No hay eventos programados para el {fecha}.")
    except ValueError as ve:
        print(f"Error en el formato de la fecha: {ve}")
    except Exception as e:
        print(f"Error al listar eventos: {e}")

#Mostrar servicios con catering en fecha especifica 
def listar_eventos_con_catering(mes, año):
    
    with Session() as session:
        eventos_catering = session.query(
            Evento.nombre,
            Evento.categoria,
            Reservacion.fecha_evento,
            ReservacionServicio.cantidad.label("num_asistentes"),
            Salon.ubicacion
        ).join(Reservacion, Evento.evento_id == Reservacion.evento_id) \
         .join(ReservacionServicio, Reservacion.reservacion_id == ReservacionServicio.reservacion_id) \
         .join(Servicio, ReservacionServicio.servicio_id == Servicio.servicio_id) \
         .join(Salon, Reservacion.salon_id == Salon.salon_id) \
         .filter(
             Servicio.nombre == 'Catering',
             extract('month', Reservacion.fecha_evento) == mes,
             extract('year', Reservacion.fecha_evento) == año
         ).all()

        for evento in eventos_catering:
            print(f"Evento: {evento.nombre}, Tipo: {evento.categoria}, "
                  f"Fecha: {evento.fecha_evento}, "
                  f"Asistentes: {evento.num_asistentes}, Ubicación: {evento.ubicacion}")
            
#Costo total de una reservacion 
def calcular_costo_total_reservacion(reservacion_id):
   
    with Session() as session:
        total_base = session.query(func.coalesce(Reservacion.tarifa_aplicada, 0)) \
                            .filter(Reservacion.reservacion_id == reservacion_id) \
                            .scalar()

        total_servicios = session.query(func.coalesce(func.sum(ReservacionServicio.costo_aplicado), 0)) \
                                 .filter(ReservacionServicio.reservacion_id == reservacion_id) \
                                 .scalar()

        costo_total = total_base + total_servicios
        print(f"Reservación {reservacion_id}: Costo Total = ${costo_total:.2f}")
        
#Obtener historial del evento 

def obtener_historial_evento(evento_id):
  
    try:
        
        historial = session.query(
            HistorialEvento.evento_historial_id,
            HistorialEvento.nombre_modificado,
            HistorialEvento.descripcion_modificada,
            HistorialEvento.fecha_modificacion,
            HistorialEvento.modificado_por
        ).filter(
            HistorialEvento.evento_id == evento_id
        ).order_by(
            HistorialEvento.fecha_modificacion.desc()
        ).all()

        # Imprimir resultados
        if historial:
            print(f"Historial de modificaciones para el evento ID {evento_id}:")
            for registro in historial:
                print(f"Fecha: {registro.fecha_modificacion}, Modificado por: {registro.modificado_por}")
                print(f"Nombre modificado: {registro.nombre_modificado}")
                print(f"Descripción modificada: {registro.descripcion_modificada}")
                print("-" * 40) 
        else:
            print(f"No se encontró historial de modificaciones para el evento ID {evento_id}.")
    except Exception as e:
        print(f"Error al obtener el historial del evento: {e}")
        
#Encontrar empleados disponibles 
def encontrar_empleados_disponibles(rol, fecha_inicio, fecha_fin):
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d %H:%M:%S')
        fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d %H:%M:%S')

        empleados_con_rol = session.query(Empleado).filter(
            Empleado.rol == rol
        ).all()
        empleados_disponibles = []

        for empleado in empleados_con_rol:
            asignaciones_conflicto = session.query(AsignacionEmpleadoEvento).filter(
                AsignacionEmpleadoEvento.empleado_id == empleado.empleado_id,
                or_(
                    and_(
                        AsignacionEmpleadoEvento.hora_inicio <= fecha_inicio,
                        AsignacionEmpleadoEvento.hora_fin >= fecha_inicio
                    ),
                    and_(
                        AsignacionEmpleadoEvento.hora_inicio <= fecha_fin,
                        AsignacionEmpleadoEvento.hora_fin >= fecha_fin
                    ),
                    and_(
                        AsignacionEmpleadoEvento.hora_inicio >= fecha_inicio,
                        AsignacionEmpleadoEvento.hora_fin <= fecha_fin
                    )
                )
            ).all()

            if not asignaciones_conflicto:
                empleados_disponibles.append(empleado)
        if empleados_disponibles:
            print(f"Empleados disponibles para el rol '{rol}' entre {fecha_inicio} y {fecha_fin}:")
            for empleado in empleados_disponibles:
                print(f"ID: {empleado.empleado_id}, Nombre: {empleado.nombre}, Contacto: {empleado.contacto}")
        else:
            print(f"No hay empleados disponibles para el rol '{rol}' entre {fecha_inicio} y {fecha_fin}.")
    except Exception as e:
        print(f"Error al encontrar empleados disponibles: {e}")
            


#call preferred function
def main():
    get_employee_byid(1)

if __name__ == "__main__":
    main()