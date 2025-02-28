from models import Evento, Cliente
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


#Change database connection data
DATABASE_URL =  "postgresql://postgres:Platano45@localhost/Hoteleria_oficial"  
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bing=engine)
session = Session()


def insert_event(evento_id, nombre, descripcion, categoria, fecha_programada, cliente_id):
    event = Evento(evento_id, nombre, descripcion, categoria, fecha_programada, cliente_id)
    session.add(event)
    session.commit()

def insert_client(nombre, direccion, telefono, email):
    client = Cliente(nombre, direccion, telefono, email)
    session.add(client)
    session.commit()