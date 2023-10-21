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
        sql = 'SELECT cedula, nombre, apellido, telefono FROM clientes WHERE cedula = {}'.format(cedula)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            if user:
                print("Cédula: ", user[0])
                print("Nombre: ", user[1])
                print("Apellido: ", user[2])
                print("Teléfono: ", user[3])
            else:
                print("Usuario con cédul {} no encontrado.".format(cedula))
                
        except Exception as e:
            raise

    def select_all_users(self):
        sql = 'SELECT cedula, nombre, apellido, telefono FROM clientes'

        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()

            for user in users:
                print("Cédula: ", user[0])
                print("Nombre: ", user[1])
                print("Apellido: ", user[2])
                print("Teléfono: ", user[3])
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

    def create_user(self):
        sql = "INSERT INTO clientes VALUES ( 10139744434, 'Natalia','Beltrán','3142897560' );"

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def close(self):
        self.connection.close()

database = DataBase()

database.select_user(1014287766)
database.update_user(1014287766, 'Guillermo')
database.select_user(1014287766)
#database.create_user()
database.select_all_users()
database.close()