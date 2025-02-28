from models import Evento, Cliente, Empleado, Salon, Servicio
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
    
]


def insert_client_data():
    try:    
        clients_objects = [Cliente(cliente_id=data[0], nombre=data[1], direccion=data[2], telefono=data[3], email=data[4]) for data in client_list]
        
        session.add_all(clients_objects)
        session.commit()

    except Exception as e:
        session.rollback()  # Deshacemos los cambios en caso de error
        print(f"Error insertando clientes: {e}")

def main():
    insert_client_data()


if __name__ == "__main__":
    main()