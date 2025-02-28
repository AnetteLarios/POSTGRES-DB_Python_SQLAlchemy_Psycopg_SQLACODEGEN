from models import Evento, Cliente, Empleado, Salon, Servicio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Change database connection data
DATABASE_URL =  "postgresql://postgres:Platano45@localhost/Hoteleria_oficial"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


#Insert 

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


def main():
    insert_event()

if __name__ == "__main__":
    main()