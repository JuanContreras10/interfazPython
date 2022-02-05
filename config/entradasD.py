import socket
import sys
from datetime import date, datetime


class SocketsD:
    
    def __init__(self):
        self.PORT = 10001
        self.HOST = "192.168.100.210"
        self.server_address = (self.HOST,self.PORT)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.conn = ""
        self.mensaje = ""
        self.diss = ""
    
    def getConexion(self):
        try:
            self.conn = self.sock.connect(self.server_address)
            print("conexion exitosa al socket direccional")
            
        except Exception as e:
            print("Error de conexion", e)
        
        return self.conn
    
    def mensajeServer(self):
        self.mensaje = self.sock.recv(1024)
        #print(mensaje)
        return self.mensaje
    
    def getDesconexion(self):
        try:
            self.diss = self.sock.close()
            print("desconexion exitosa direccional")
        
        except: 
            print("No se ha desconectado")
        
        return self.diss

