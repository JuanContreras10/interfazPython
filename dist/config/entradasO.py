import socket
import sys
from datetime import date, datetime


class SocketsO:
    
    def __init__(self):
        self.PORT = 10001
        self.HOST = "192.168.100.211"
        self.server_address = (self.HOST,self.PORT)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def getConexion(self):
        try:
            conn = self.sock.connect(self.server_address)
            print("conexion exitosa al socket Omnidireccional")
            
        except Exception as e:
            print("Error de conexion", e)
        
        return conn
    
    def mensajeServer(self):
        mensaje = self.sock.recv(1024)
        #print(mensaje)
        return mensaje
    
    def getDesconexion(self):
        try:
            diss = self.sock.close()
            print("desconexion exitosa Omnidireccional")
        
        except: 
            print("No se ha desconectado")
        
        return diss

'''
tiempoDuracion = 60
so = Sockets()
tiempo = datetime.now()
so.getConexion()

while (datetime.now() - tiempo).seconds <= (tiempoDuracion - 0.5):
    
    mensajeServidor = so.mensajeServer()
    arregloCompleto = str(mensajeServidor).split('\\')
    
    #print(arregloCompleto)
    #print(len(arregloCompleto))
    
    if(len(arregloCompleto) > 1):
        
        primerValor = arregloCompleto[1]
        finalValor = str(mensajeServidor)[-2]
        
        #print(primerValor)
        #print(finalValor)
        #print(primerValor[0:3])
        #print(len(arregloCompleto))
        
        if(primerValor[0:3] == "xaa" and len(arregloCompleto) > 2):
            
            #print(arregloCompleto[2][0:3])
            
            if(arregloCompleto[2][0:3] == "x0f"):
                if(primerValor[0:3] == "xaa" and finalValor == "D"):
                    
                   arregloFinal = str(mensajeServidor).split('\\',12)
                   
                   #print(arregloFinal)
                   #print(len(arregloFinal))
                   
                   if(len(arregloFinal) > 8):
                       tagH1 = arregloFinal[8]
                       tagH1s = tagH1[1:3]
                       tagH2 = arregloFinal[9]
                       tagH2s = tagH2[1:3]
                       
                       #print(tagH1s)
                       #print(tagH2s)
                       
                       resultado = int(tagH1s + tagH2s, 16)
                       resultadoString = str(resultado)
                       
                       print(resultadoString)
                       
                       if(len(resultadoString) != 4):
                            tagH1 = arregloFinal[9]
                            tagH1s = tagH1[1:3]
                            tagH2 = arregloFinal[10]
                            tagH2s = tagH2[1:3]
                            
                            #print(tagH1s)
                            #print(tagH2s)
                            
                            resultado = int(tagH1s + tagH2s, 16)
                            resultadoString = str(resultado)
                            print(resultadoString)

                   
                     
so.getDesconexion()
'''

'''               
# Crear socket
socketConexion = socket.socket()
 
# Servidor de conexión
servidor = "192.168.100.210"
# El puerto a utilizar (el servidor debe estar escuchando en este puerto)
puerto = 10001
 
try:
    # Conectar el socket del cliente con el servidor en el puerto indicado
    socketConexion.connect((servidor, puerto))
except socket.error as message:
    print("Falló la conexión con el servidor {} por el puerto {}".format(servidor, puerto))
    print(message)
    sys.exit()  
 
# Recibir y mostrar el mensaje del servidor

tiempoDuracion = 60
t1 = datetime.now()

while (datetime.now()-t1).seconds <= (tiempoDuracion - 0.5):
    mensajeServidor = socketConexion.recv(1024)
    mensajeServidor = str(mensajeServidor).split('\\',12)
    #print(mensajeServidor)
    print(len(mensajeServidor))
    if(len(mensajeServidor)) > 8 :
        tagH1 = mensajeServidor[8]
        tagH1s=tagH1[1:3]
        tagH2=mensajeServidor[9]
        #print(tagH2)
        tagH2s=tagH2[1:3]
        #print(tagH1s)
        #print(tagH2s)
        res = int(tagH1s+tagH2s,16)
        cadena = str(res)
        print(cadena)
        if(len(cadena)!=4):
            tagH1=mensajeServidor[9]
            tagH1s=tagH1[1:3]
            tagH2=mensajeServidor[10]
            tagH2s=tagH2[1:3]
            res=int(tagH1s+tagH2s,16)
'''

'''
t1 = datetime.now()
print(tiempoDuracion-.5)
print ((datetime.now()-t1).seconds)
print(t1)
mensajeServidor = str(mensajeServidor).split('\\')
print(mensajeServidor)

primerValor = mensajeServidor[2][0:3]
finalValor = str(mensajeServidor)[-4]
print(len(primerValor))
print(finalValor)

x = str(mensajeServidor).split('\\',12)
print(len(x))

print(primerValor)
print(len(primerValor))

'''
# Cerrar el socket
#socketConexion.close()
'''
 if(len(mensajeServidor)) > 8 :
        tagH1 = mensajeServidor[8]
        tagH1s=tagH1[1:3]
        #print(tagH1)
        print(tagH1s)
        tagH2=mensajeServidor[9]
        #print(tagH2)
        tagH2s=tagH2[1:3]
        #print(tagH1s)
        print(tagH2s)
        print(tagH1s + tagH2s)
        res = int(tagH1s+tagH2s,16)
        #print(res)
        cadena = str(res)
        #print(cadena)
        if(len(cadena)!=4):
            tagH1=mensajeServidor[9]
            tagH1s=tagH1[1:3]
            tagH2=mensajeServidor[10]
            tagH2s=tagH2[1:3]
            res=int(tagH1s+tagH2s,16)
            #print(res)
'''