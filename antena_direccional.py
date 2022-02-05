import sys
sys.path.append('./config')

import time

from entradasD import SocketsD
from entradasO import SocketsO
from database import Database
from datetime import date, datetime



class appDao:
      
      def __init__(self):
           self.db = Database()
           self.conexion = self.db.getconexion()
           


      def updateO(self, resultadoFinal):
        cursor2 = self.conexion.cursor()
        queryupdate = "UPDATE pruebas_omnidireccional SET tag=%s, hora_tag=%s WHERE hora_inicial=%s"
        datosIngresarTag = (resultadoFinal[0],resultadoFinal[2],tiempoCorriendoString)
        cursor2.execute(queryupdate,datosIngresarTag)
        self.conexion.commit()

      def updateD(self, resultadoFinal):
        cursor2 = self.conexion.cursor()
        queryupdate = "UPDATE pruebas_direccional SET tag=%s, hora_tag=%s WHERE hora_inicial=%s"
        datosIngresarTag = (resultadoFinal[0],resultadoFinal[2],tiempoCorriendoString)
        cursor2.execute(queryupdate,datosIngresarTag)
        self.conexion.commit()
        
      def insersionD(self, nombreAntenaD,distancia,muestra,fecha,tiempoCorriendo,tag,hora_inicial, segundos):
        cursor = self.conexion.cursor()
        query = "insert into pruebas_direccional(antena, metraje, prueba, fecha, hora_inicial, tag, hora_tag,tiempo_estimado) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        datosIngresar = (nombreAntenaD,distancia,muestra,fecha,tiempoCorriendo,tag,hora_inicial,segundos)
        cursor.execute(query,datosIngresar)              
        self.conexion.commit() 

      def insersionO(self, nombreAntenaO,distancia,muestra,fecha,tiempoCorriendo,tag,hora_inicial, segundos):
        cursor = self.conexion.cursor()
        query = "insert into pruebas_omnidireccional(antena, metraje, prueba, fecha, hora_inicial, tag, hora_tag, tiempo_estimado) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        datosIngresar = (nombreAntenaO,distancia,muestra,fecha,tiempoCorriendo,tag,hora_inicial,segundos)
        cursor.execute(query,datosIngresar)              
        self.conexion.commit()
      

class Servicio:

    def __init__(self, idPrueba, antNombre, metraje, tag, segundos):
        #self.antenaDireccional = "D" #nombre
        #self.antenaOnm = "O" #nombre
        #self.altura = "12" #altura

        self.muestra = "01" #idPrueba
        self.nombreAntenaD = antNombre
        self.nombreAntenaO = antNombre
        self.distancia = metraje #metraje
        self.tag = tag
        self.hora_inicial = " "

        self.tiempoDuracion = segundos 

        self.soD = SocketsD()
        self.soO = SocketsO()
       
        self.tiempo = datetime.now()
        self.fecha = str(date.today())
        self.localtime = time.localtime()

        self.soD.getConexion()
        self.soO.getConexion()
    
    def imprimirvalorO(self, arregloFinal, tiempoCorriendoString1):
        crudDao = appDao()
        if(len(arregloFinal) > 8):
                        tagH1 = arregloFinal[8]
                        tagH1s = tagH1[1:3]
                        tagH2 = arregloFinal[9]
                        tagH2s = tagH2[1:3]
                        
                        #print(tagH1s)
                        #print(tagH2s)
                        
                        resultado = int(tagH1s + tagH2s, 16)
                        resultadoString = str(resultado)
                        resultadoFinal = str(resultadoString + " " + self.fecha + " " + tiempoCorriendoString1).split(" ")
                        
                        crudDao.updateO(resultadoFinal)
                        
                        #resultadoString[0] = tag
                        #resultadoString[2] = hora_inicial
                        
                        #print(resultadoFinal[0])
                        #print(hora_inicial)
                        
                        #print(resultadoFinal)                       
                        print(resultadoFinal)
                                                
                        if(len(resultadoString) != 4):
                                tagH1 = arregloFinal[9]
                                tagH1s = tagH1[1:3]
                                tagH2 = arregloFinal[10]
                                tagH2s = tagH2[1:3]
                                
                                #print(tagH1s)
                                #print(tagH2s)
                                
                                resultado = int(tagH1s + tagH2s, 16)
                                resultadoString = str(resultado)
                                resultadoFinal = str(resultadoString + " " + self.fecha + " " + tiempoCorriendoString1).split(" ")
                                
                                crudDao.updateO(resultadoFinal)
                                
                                #resultadoString[0] = tag
                                #resultadoString[2] = hora_inicial
                                
                                #print(tag)
                                #print(hora_inicial)
                                print(resultadoFinal)

    def imprimirvalorD(self,arregloFinal, tiempoCorriendoString1):
        crudDao = appDao()
        if(len(arregloFinal) > 8):
                        tagH1 = arregloFinal[8]
                        tagH1s = tagH1[1:3]
                        tagH2 = arregloFinal[9]
                        tagH2s = tagH2[1:3]
                        
                        #print(tagH1s)
                        #print(tagH2s)
                        
                        resultado = int(tagH1s + tagH2s, 16)
                        resultadoString = str(resultado)
                        resultadoFinal = str(resultadoString + " " + self.fecha + " " + tiempoCorriendoString1).split(" ")
                        
                        crudDao.updateD(resultadoFinal)
                        
                        #resultadoString[0] = tag
                        #resultadoString[2] = hora_inicial
                        
                        #print(resultadoFinal[0])
                        #print(hora_inicial)
                        
                        #print(resultadoFinal)                       
                        print(resultadoFinal)
                                                
                        if(len(resultadoString) != 4):
                                tagH1 = arregloFinal[9]
                                tagH1s = tagH1[1:3]
                                tagH2 = arregloFinal[10]
                                tagH2s = tagH2[1:3]
                                
                                #print(tagH1s)
                                #print(tagH2s)
                                
                                resultado = int(tagH1s + tagH2s, 16)
                                resultadoString = str(resultado)
                                resultadoFinal = str(resultadoString + " " + self.fecha + " " + tiempoCorriendoString1).split(" ")
                                
                                crudDao.updateD(resultadoFinal)
                                
                                #resultadoString[0] = tag
                                #resultadoString[2] = hora_inicial
                                
                                #print(tag)
                                #print(hora_inicial)
                                print(resultadoFinal)

    def obtenerValorO(self, arregloCompletoO, tiempoCorriendoString1):
        if(len(arregloCompletoO) > 1):
            
            primerValor = arregloCompletoO[1]
            finalValor = str(mensajeServidorO)[-2]
            
            #print(primerValor)
            #print(finalValor)
            #print(primerValor[0:3])
            #print(len(arregloCompleto))
            
            if(primerValor[0:3] == "xaa" and len(arregloCompletoO) > 2):
                
                #print(arregloCompleto[2][0:3])
                
                if(arregloCompletoO[2][0:3] == "x0f"):
                    if(primerValor[0:3] == "xaa" and finalValor == "D"):
                        
                     arregloFinal = str(mensajeServidorO).split('\\',12)
                    
                     self.imprimirvalorO(arregloFinal, tiempoCorriendoString1)
                    #print(arregloFinal)
                    #print(len(arregloFinal))
                    
    def obtenerValorD(self, arregloCompletoD, tiempoCorriendoString1):
        if(len(arregloCompletoD) > 1):
            
            primerValor = arregloCompletoD[1]
            finalValor = str(mensajeServidorD)[-2]
            
            #print(primerValor)
            #print(finalValor)
            #print(primerValor[0:3])
            #print(len(arregloCompleto))
            
            if(primerValor[0:3] == "xaa" and len(arregloCompletoD) > 2):
                
                #print(arregloCompleto[2][0:3])
                
                if(arregloCompletoD[2][0:3] == "x0f"):
                    if(primerValor[0:3] == "xaa" and finalValor == "D"):
                        
                     arregloFinal = str(mensajeServidorD).split('\\',12)
                    
                     self.imprimirvalorD(arregloFinal, tiempoCorriendoString1)
                    #print(arregloFinal)
                    #print(len(arregloFinal))

    def servicioFuncion(self):
        crudDao = appDao()
        while (datetime.now() - self.tiempo).seconds <= ( float(self.tiempoDuracion) - 0.5):
                
                mensajeServidorD = self.soD.mensajeServer()
                mensajeServidorO =  self.soO.mensajeServer()
                arregloCompletoD = str(mensajeServidorD).split('\\')
                arregloCompletoO = str(mensajeServidorO).split('\\')
                
                ahora = datetime.now()
                tiempoCorriendo = ahora.strftime("%H:%M:%S")
                tiempoCorriendoString = str(tiempoCorriendo)
                
                print(tiempoCorriendoString)
                
                crudDao.insersionD(self.nombreAntenaD, self.distancia, self.muestra, self.fecha, tiempoCorriendo, self.tag, self.hora_inicial,  self.tiempoDuracion)
                crudDao.insersionO(self.nombreAntenaO,self.distancia,self.muestra,self.fecha,tiempoCorriendo,self.tag,self.hora_inicial,  self.tiempoDuracion)
                
                self.obtenerValorD(arregloCompletoD,tiempoCorriendoString)
                self.obtenerValorO(arregloCompletoO,tiempoCorriendoString)

                #print(arregloCompleto)
                #print(len(arregloCompleto))
                
                
                                                    
                time.sleep(1)
                                         
        self.soD.getDesconexion()
        self.soO.getDesconexion()
        
   
