import pymysql
global conn
class Database:
    
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = ''
        self.db = 'pruebas_campo'
      
    
    def getconexion(self):
      
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   passwd=self.password,
                                   db=self.db)
            print('Conexion exitosa a la base de datos')
            
        except Exception as e:
            print("Error de conexion", e)
            
        return conn
      
