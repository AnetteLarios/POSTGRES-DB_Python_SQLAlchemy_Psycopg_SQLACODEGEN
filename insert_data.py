from models import Evento, Cliente, Empleado, Salon, Servicio, Divisa, TemporadaTarifa, ReservacionServicio, Reservacion, TransaccionDivisa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Change database connection data
DATABASE_URL =  "postgresql://postgres:Platano45@localhost/Hoteleria_oficial"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

client_list = [
    [1, 'Julio Perez Hernandez', 'Isla Cubana 2546', '5241789652', 'julioperez25@gmail.com'],
    [2, 'Maria Lopez Gomez', 'Avenida Reforma 1023', '5532147896', 'maria.lopez@gmail.com'],
    [3, 'Carlos Ramirez Torres', 'Calle Principal 456', '5614789652', 'carlos.ramirez@yahoo.com'],
    [4, 'Ana Gonzalez Chavez', 'Boulevard del Sol 789', '5512364789', 'ana.gonzalez@hotmail.com'],
    [5, 'Roberto Fernandez Diaz', 'Calle Juárez 321', '5554781236', 'roberto.fernandez@outlook.com'],
    [6, 'Laura Martinez Rojas', 'Colonia Centro 852', '5614789235', 'laura.martinez@gmail.com'],
    [7, 'Miguel Sanchez Ortega', 'Residencial Las Lomas 159', '5578945632', 'miguel.sanchez@yahoo.com'],
    [8, 'Patricia Castro Ruiz', 'Urbanización San Pedro 753', '5689741256', 'patricia.castro@live.com'],
    [9, 'Fernando Herrera Mendez', 'Paseo de la Reforma 951', '5514789654', 'fernando.herrera@gmail.com'],
    [10, 'Gabriela Vargas Soto', 'Zona Industrial 369', '5647895123', 'gabriela.vargas@hotmail.com'],
    [11, 'Ricardo Dominguez Peña', 'Calle del Bosque 741', '5598741236', 'ricardo.dominguez@outlook.com']
]

event_list = [
    [1, 'Conferencia Tech 2025', 'Evento sobre innovación tecnológica y startups', 'Conferencia', '2025-03-15 09:00:00', 1],
    [2, 'Boda María & Luis', 'Boda con temática vintage en un jardín', 'Boda', '2025-06-21 18:00:00', 2],
    [3, 'Reunión Empresarial 2025', 'Encuentro de ejecutivos para planificación anual', 'Reunion Corporativa', '2025-02-10 14:00:00', 3],
    [4, 'Cena Privada Gourmet', 'Cena exclusiva con degustación de platillos internacionales', 'Cena privada', '2025-07-04 20:30:00', 4],
    [5, 'Congreso de Marketing Digital', 'Tendencias y estrategias digitales para negocios', 'Conferencia', '2025-09-12 10:00:00', 5],
    [6, 'Boda Laura & Miguel', 'Ceremonia en la playa con recepción al atardecer', 'Boda', '2025-05-30 17:00:00', 6],
    [7, 'Convención de Negocios', 'Reunión de empresarios e inversores para nuevas oportunidades', 'Reunion Corporativa', '2025-04-22 16:00:00', 7],
    [8, 'Cena de Gala de Fin de Año', 'Evento formal para celebrar el cierre del año', 'Cena privada', '2025-12-20 21:00:00', 8],
    [9, 'Foro de Innovación en Salud', 'Charlas y paneles sobre avances en medicina', 'Conferencia', '2025-08-17 11:00:00', 9],
    [10, 'Boda Gabriela & Daniel', 'Fiesta elegante con recepción en salón exclusivo', 'Boda', '2025-10-14 19:00:00', 10],
    [11, 'Reunión de Directivos', 'Estrategias de negocio y evaluación anual de desempeño', 'Reunion Corporativa', '2025-11-05 15:00:00', 11]
]


employee_list = [
    [1, 'Juanito Perez Lopez', '1542637895', 2, 'Mesero'],
    [2, 'Maria Gonzalez Ruiz', '5547896321', 3, 'Coordinador'],
    [3, 'Carlos Fernandez Soto', '4789651236', 1, 'Chef'],
    [4, 'Ana Ramirez Torres', '3698745214', 5, 'Musico'],
    [5, 'Miguel Dominguez Chavez', '5623147896', 4, 'Mesero'],
    [6, 'Laura Martinez Ortega', '7854123695', 2, 'Coordinador'],
    [7, 'Roberto Herrera Peña', '6958741235', 3, 'Chef'],
    [8, 'Patricia Vargas Lopez', '2145698732', 5, 'Musico'],
    [9, 'Fernando Castro Rojas', '8956321475', 1, 'Mesero'],
    [10, 'Gabriela Soto Mendez', '3658749125', 4, 'Coordinador'],
    [11, 'Ricardo Dominguez Peña', '1596324785', 2, 'Chef']
]

currency_list = [
    [1, 'EUR', 'Euro'],
    [2, 'MXN', 'Pesos Mexicanos'],
    [3, 'USD', 'Dolar Estadounidense']
]


hall_list = [
    [1, 'Salon de eventos Galaxia', 'Isla Catalina 2645', 250],
    [2, 'Gran Salon Estrella', 'Avenida Central 1023', 500],
    [3, 'Salon Luna Llena', 'Calle del Sol 456', 300],
    [4, 'Eventos Aurora', 'Boulevard Celestial 789', 600],
    [5, 'Salón Diamante', 'Calle Juárez 321', 450],
    [6, 'Espacio Elegante', 'Colonia Centro 852', 700],
    [7, 'Fiestas del Bosque', 'Residencial Las Lomas 159', 350],
    [8, 'Salón Real', 'Urbanización San Pedro 753', 650],
    [9, 'Eventos Premium', 'Paseo de la Reforma 951', 400],
    [10, 'Salón Dorado', 'Zona Industrial 369', 750]
]

service_list = [
    [1, 'Catering', 'Para evento relacionado', 1250.00],
    [2,'Música en vivo', 'Para evento relacionado', 1550.00],
    [3, 'Decoración temática', 'Para evento relacionado', 1185.00]
]

currency_season_list = [
    [1,'2025-06-01', '2025-08-31', 1.20, 'Temporada alta de verano'],
    [2,'2025-09-01', '2025-11-30', 0.90, 'Temporada baja de otoño'],
    [3, '2025-12-01', '2026-01-15', 1.50, 'Temporada alta de invierno'],
    [4, '2026-01-16', '2026-03-31', 1.00, 'Temporada regular de inicio de año'],
    [5, '2026-04-01', '2026-05-31', 1.10, 'Temporada media de primavera']

]

reservation_list = [
   [1, 1,1, '2025-06-15 18:00:00', '2025-07-15', None, 2, '[2025-06-15 18:00:00, 2025-06-15 23:00:00]', 5000.00 * 1.10],
   [2, 3,2, '2025-07-10 19:00:00','2025-09-12', None, 4, '[2025-07-10 19:00:00, 2025-07-10 23:59:59]', 7000.00 * 0.90],
   [5, 6,4 ,'2025-10-12 20:00:00','2025-11-12', None, 5, '[2025-10-12 20:00:00, 2025-10-13 01:00:00]', 8000.00 * 1.1],
   [4, 2,5 ,'2025-09-25 17:30:00','2025-10-12', None, 3, '[2025-09-25 17:30:00, 2025-09-25 22:30:00]', 6200.00 * 1.00],
   [3, 5,6 ,'2025-08-05 16:00:00','2025-09-07', None, 1, '[2025-08-05 16:00:00, 2025-08-05 21:00:00]', 4500.00 * 0.90]

]

service_reservation_list = [
    [1, 1, 1, 1250.00 * 1],  
    [2, 2, 1, 1550.00 * 1], 
    [3, 3, 1, 1185.00 * 1],  
    [4, 1, 2, 1250.00 * 2], 
    [5, 2, 1, 1550.00 * 1]
]

invoice_list = [
    [1, 1, 6000.00, '2025-06-15 19:00:00', 'MXN', 1.20, 0, 0, 5000.00 * 1.20],  
    [2, 2, 350.00 *18, '2025-07-10 19:30:00', 'USD', 0.90, 0, 0, (7000.00 * 0.90) / 18],  
    [3, 3, 600.00 *20, '2025-12-05 20:30:00', 'EUR', 1.50, 0, 0, (8000.00 * 1.50) / 20],  
    [4, 4, 6200, '2025-09-25 17:45:00', 'MXN', 1.00, 0, 0, 6200.00 * 1.00],  
    [5, 5, 275.00*18, '2025-08-05 16:30:00', 'USD', 1.10, 0, 0, (4500.00 * 1.10) / 18]
]

transaccion_divisa_list = [
    [1, 2, "now()", "compra", "USD", "MXN", 18.0000],  
    [2, 3, "now()", "compra", "EUR", "MXN", 20.0000],  
    [3, 5, "now()", "compra", "USD", "MXN", 18.0000]   
]

def insert_client_data():
    try:    
        clients_objects = (Cliente(cliente_id=data[0], nombre=data[1], direccion=data[2], telefono=data[3], email=data[4]) for data in client_list)
        session.add_all(clients_objects)
        session.commit()

    except Exception as e:
        session.rollback( ) # Deshacemos los cambios en caso de error
        print(f"Error insertando clientes: {e}")

def insert_event_data():
    try: 
        events_objects = (Evento(evento_id=data[0], nombre=data[1], descripcion=data[2], categoria=data[3], fecha_programada=data[4], cliente_id=data[5])for data in event_list)
        session.add_all(events_objects)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error insertando eventos: {e}")

def insert_employee_data():
    try:
        employee_objects = (Empleado(empleado_id = data[0], nombre = data[1], contacto = data[2], jerarquia = data[3], rol = data[4]) for data in employee_list) 
        session.add_all(employee_objects)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error insertado empleados: {e}")

def insert_currency_data():
    try:
        currency_objects = (Divisa(divisa_id = data[0], codigo = data[1], nombre = data[2]) for data in currency_list)
        session.add_all(currency_objects)
        session.commit()
    except Exception as e:
        print(f"Error insertando divisas: {e}")

def insert_hall_data():
    try:
        hall_objects = (Salon(salon_id = data[0], nombre = data [1], ubicacion = data[2], capacidad = data[3]) for data in hall_list)
        session.add_all(hall_objects)
        session.commit()
    except Exception as e:
        print(f"Error insertando salones: {e}")

def insert_service_data():
    try:
        service_objects = (Servicio(servicio_id = data[0], nombre = data[1], descripcion = data[2], costo_base = data[3])for data in service_list)
        session.add_all(service_objects)
        session.commit()
    except Exception as e:
        print(f"Eror al insertar sercicios: {e}")

def insert_currency_season():
    try:
        currency_objects = (TemporadaTarifa(temporada_id = data[0], fecha_inicio=data[1], fecha_fin=data[2], modificador_tarifa=data[3], descripcion=data[4])for data in currency_season_list)
        session.add_all(currency_objects)
        session.commit()
    except Exception as  e:
        print(f"Error insertando tarifa de temporada {e}")



def insert_reservation():
    try:
        reservation_objects = (Reservacion(reservacion_id = data[0], evento_id = data[1], cliente_id = data[2], fecha_solicitud = data[3], fecha_evento =data[4], fecha_cancelacion = data[5], salon_id=data[6], rango_horario=data[7], tarifa_aplicada=data[8]
                                        )for data in reservation_list)
        session.add_all(reservation_objects)
        session.commit()
    except Exception as e:
        print(f"Error insertando reservacion {e}")



def insert_service_reservation():
    try:
        service_reservation_objects = (ReservacionServicio(reservacion_id = data[0], servicio_id = data[1], cantidad = data[2], costo_aplicado = data[3]) for data in service_reservation_list)
        session.add_all(service_reservation_objects)
        session.commit()
    except Exception as e:
        print(f"Error insertando servicios de reservacion: {e}") 



def insert_invoice():
    try:
        invoice_objects = (ReservacionServicio(factura_id = data[0], reservacion_id = data[1], total = data[2], fecha_pago = data[3], moneda =data[4], tasa_cambio = data[5], descuento=data[6], penalizacion=data[7], monto_convertido=data[8]
                                        )for data in invoice_list) 
        session.add_all(invoice_objects)
        session.commit()
    except Exception as e:
        print(f"Error insertando facturas: {e}") 

def insert_currency_transaction():
    try:
        transaction_objects = (TransaccionDivisa(transaccion_id = data[0],factura_id = data[1], fecha_transaccion = data[2], tipo_transaccion = data[3], moneda_origen =data[4], moneda_destino = data[5], tasa_aplicada=data[6])for data in transaccion_divisa_list) 
        session.add_all(transaction_objects)
        session.commit()
    except Exception as e:
        print(f"Error insertando transacciones: {e}") 

#Call the function to populate the table you want
def main():
    #insert_client_data()
    insert_currency_transaction()

if __name__ == "__main__":
    main()