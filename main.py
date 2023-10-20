import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            db='parqueadero'
        )
        self.cursor = self.connection.cursor()

        print('Conexión establecida exitosamente')

    def select_user(self, cedula):
        sql = 'SELECT cedula, nombre, telefono FROM clientes WHERE cedula = {}'.format(cedula)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print("Cédula: ", user[0])
            print("Nombre: ", user[1])
            print("Teléfono: ", user[2])

        except Exception as e:
            raise

    def select_all_users(self)        
        sql = 'SELECT cedula, nombre, telefono FROM clientes'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for user in users:
                print("Cédula: ", user[0])
                print("Nombre: ", user[1])
                print("Teléfono: ", user[2])
                print("______\n")

        except Exception as e:
            raise
    
    def update_user(self, cedula, nombre):
        sql = "UPDATE clientes SET nombre = '{}' WHERE cedula = {}".format(nombre, cedula)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise

database = DataBase()
database.select_user(1)
database.update_user(1, 'Guillermo')
database.select_user(1)
