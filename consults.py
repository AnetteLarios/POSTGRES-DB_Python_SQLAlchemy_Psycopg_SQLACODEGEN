from models import Evento, Cliente, Empleado, Salon, Servicio, Divisa, TemporadaTarifa, ReservacionServicio, Servicio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

#call preferred function
def main():
    update_employee()

if __name__ == "__main__":
    main()