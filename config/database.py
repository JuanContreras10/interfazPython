import pymysql

class Database:
    
    def __init__(self):
        self.host = '192.168.100.42'
        self.user = 'root'
        self.password = ''
        self.db = 'pruebas_campo'
        self.conn = pymysql.connect()
    
    def getconexion(self):
        self.conn
        try:
            self.conn = pymysql.connect(host=self.host,
                                   user=self.user,
                                   passwd=self.password,
                                   db=self.db)
            print('Conexion exitosa a la base de datos')
            
        except Exception as e:
            print("Error de conexion", e)
            
        return self.conn
      
