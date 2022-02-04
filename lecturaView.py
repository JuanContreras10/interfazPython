import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk


root = tk.Tk()
#nombre ventana
root.title("Lecturas")


# label en ventana
tituloLabel = tk.Label(root, text="Lecturas")
idPruebaLabel = tk.Label(root,text="ID Prueba:")
antLabel = tk.Label(root, text="Ant:")
metrajeLabel = tk.Label(root, text="Metraje:")

tag1Label = tk.Label(root, text="Tag 1:")
tag2Label = tk.Label(root, text="Tag 2:")
tag3Label = tk.Label(root, text="Tag 3:")
segubdoLabel = tk.Label(root, text="Seg:")

#configuracion pantallaprincipal
def configWindow():
    #tamaño y pos de pantalla
    anchoVentana = 600
    altoVentana = 150

    xVentana = root.winfo_screenwidth() // 2 - anchoVentana // 2
    yVentana = root.winfo_screenheight() // 2 - altoVentana // 2

    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(xVentana) + "+" + str(yVentana)

    root.geometry(posicion)
    root.resizable(0, 0)

    #root.rowconfigure(0, weight=1)

    root.columnconfigure(1, weight=2)
    root.columnconfigure(3, weight=2)
    root.columnconfigure(5, weight=2)

#configuracion pantalla 2
def configWindow2(idPrueba,ant,metraje,tag1,tag2,tag3,segundo):
    #tamaño y pos de pantalla
    pantallaResultado = Toplevel()
    
    pantallaResultado.title("Resultados")
    anchoVentana = 250
    altoVentana = 350

    xVentana = pantallaResultado.winfo_screenwidth() // 2 - anchoVentana // 2
    yVentana = pantallaResultado.winfo_screenheight() // 2 - altoVentana // 2

    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(xVentana+10) + "+" + str(yVentana+10)

    pantallaResultado.geometry(posicion)
    #pantallaResultado.resizable(0, 0)

    def cerrar():
        pantallaResultado.destroy()



    pruebaLabel = tk.Label(pantallaResultado, text="idPrueba: " + idPrueba)
    antLabel = tk.Label(pantallaResultado, text="Antena: " + ant)
    metrajeLabel = tk.Label(pantallaResultado, text="Metraje: " + metraje)
    tag1Label = tk.Label(pantallaResultado, text="Tag 1: " + tag1)
    tag2Label = tk.Label(pantallaResultado, text="tag 2: " + tag2)
    tag3Label = tk.Label(pantallaResultado, text="Tag 3: " + tag3)
    segundoLabel = tk.Label(pantallaResultado, text="Segundos: " + segundo +" s")    
    tituloLecturaLabel = tk.Label(pantallaResultado, text="Lecturas")
    lecturaBtn= tk.Button(pantallaResultado, text="Nueva Lectura",bg="#3498DB", fg="white", command = cerrar)
  


    pruebaLabel.grid(pady=(10,5), padx=5, row=0, column=0)
    antLabel.grid(pady=(10,5), padx=5, row=1, column=0)
    metrajeLabel.grid(pady=(10,5), padx=5, row=2, column=0)
    segundoLabel.grid(pady=(10,5), padx=10, row=3, column=0)
    tag1Label.grid(pady=(10,5), padx=5, row=0, column=1)
    tag2Label.grid(pady=(10,5), padx=10, row=1, column=1)
    tag3Label.grid(pady=(10,5), padx=10, row=2, column=1)
    lecturaBtn.grid(pady=(20,5), padx=(20,20),  row=3, column=1)
    tituloLecturaLabel.grid(pady=(20,5), padx=(20,20),  row=4, columnspan=2)

    lst = [
        "0001",
        "0002",
        "0003",
        "0004",
        "0005"
    ] 
   
    rows = len(lst) 
    
    for i in range(rows): #Rows 
         valor = StringVar()
         valor.set(lst[i])
         row = Entry(pantallaResultado, textvariable=valor, fg='blue',state=DISABLED) 
         row.grid(row=5+i,padx=5,pady=2, columnspan=2) 
         
#pantalla alerta
def configWindow3():
    #tamaño y pos de pantalla
    pantallaAlerta = Toplevel()
    
    pantallaAlerta.title("Alerta")
    anchoVentana = 200
    altoVentana = 200

    xVentana = pantallaAlerta.winfo_screenwidth() // 2 - anchoVentana // 2
    yVentana = pantallaAlerta.winfo_screenheight() // 2 - altoVentana // 2

    posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(xVentana+10) + "+" + str(yVentana+10)

    pantallaAlerta.geometry(posicion)
    pantallaAlerta.resizable(0, 0)

    
    pruebaLabel = tk.Label(pantallaAlerta, text="Algunos Campos Estan Vacios")
    imagen = "asssets/wngCirculo-PhotoRoom.png"
    image = Image.open(imagen)
    resizeImage = image.resize((120, 120))
 
    img = ImageTk.PhotoImage(resizeImage)
    label1 = tk.Label(pantallaAlerta,image=img)
    label1.image = img
    


    pruebaLabel.grid(pady=(30,5), padx=5, row=0, column=0)
    label1.grid(pady=(30,5), padx=5, row=1, column=0)
  
#validaciones
def validarIdPrueba(text):
    return text.isdecimal()

#obtencion de datos
def obtenerParametros():
    idPrueba = idPruebaEntry.get()
    ant = antEntry.get()
    metraje = metajeCombo.get()
    tag1 = tagEntry1.get()
    tag2 = tagEntry2.get()
    tag3 = tagEntry3.get()
    segundo = segCombo.get()
    isCompleto = True


    if idPrueba == "" :
        isCompleto = False

    if ant == "" :
        isCompleto = False

    if metraje == "" :
        isCompleto = False

    if tag1 == "" :
        isCompleto = False 

    #    if tag2 == "" :
    #        isCompleto = False    

    #    if tag3 == "" :
    #        isCompleto = False

    if segundo == "" :
        isCompleto = False
               

    if isCompleto :
        print(idPrueba + ant + metraje + tag1 + tag2 + tag3 + segundo)
        configWindow2(idPrueba,ant,metraje,tag1,tag2,tag3,segundo)
        
    else :     
        configWindow3()
        print("campo vacio")

#variables set
segundosLista = ['60', '120', '180','240','300']
segundoSet = tk.StringVar(root)
segundoSet.set('60')

metrajeLista = ['160','150','140','130','120','110','100','90','80','70','60','50','40','30','20','10','0','-10','-20','-30','-40','-50','-60','-70','-80','-90','-100','110','-120','-130','-140','-150','-160']
metrajeSet = tk.StringVar(root)
metrajeSet.set('160')
#widgets 
idPruebaEntry = ttk.Entry(root,   validate="key",
    validatecommand=(root.register(validarIdPrueba), "%S"))

antEntry = ttk.Entry(root,  validate="key",
    validatecommand=(root.register(validarIdPrueba), "%S"))

metajeCombo =  ttk.Combobox(root,values = metrajeLista, textvariable=metrajeSet)

segCombo = ttk.Combobox(root,values = segundosLista,  textvariable=segundoSet)

tagEntry1 = ttk.Entry(root,   validate="key",
    validatecommand=(root.register(validarIdPrueba), "%S"))

tagEntry2 = ttk.Entry(root, state=DISABLED,   validate="key",
    validatecommand=(root.register(validarIdPrueba), "%S"))

tagEntry3 = ttk.Entry(root, state=DISABLED,  validate="key",
    validatecommand=(root.register(validarIdPrueba), "%S"))

#botones
lecturaBtn= tk.Button(root, text="Ejecutar Lectura",bg="#3498DB", fg="white", command = obtenerParametros)




# cuerpo de ventana principal
def body():
    idPruebaLabel.grid(pady=(30,5), padx=5, row=0, column=0)
    idPruebaEntry.grid(pady=(30,5), padx=(2,20),  row=0, column=1)

    antLabel.grid(pady=(30,5), padx=5,  row=0, column=2)
    antEntry.grid(pady=(30,5), padx=(2,20),  row=0, column=3)

    metrajeLabel.grid(pady=(30,5), padx=5 , row=0 , column=4)
    metajeCombo.grid(pady=(30,5), padx=(2,20) , row=0 , column=5)

   
    tag1Label.grid(pady=(10,5) ,  row=1 , column=0)
    tagEntry1.grid(pady=(10,5), padx=(2,20) ,  row=1 , column=1)
    tag2Label.grid(pady=(10,5) ,  row=1 , column=2)
    tagEntry2.grid(pady=(10,5), padx=(2,20) ,  row=1 , column=3)
    tag3Label.grid(pady=(10,5) ,  row=1 , column=4)
    tagEntry3.grid(pady=(10,5), padx=(2,20) ,  row=1 , column=5)

    segubdoLabel.grid(pady=(20,5), padx=5 ,  row=2, column=0)
    segCombo.grid(pady=(20,5), padx=(2,20),  row=2, column=1)
    #botones    
    lecturaBtn.grid(pady=(20,5), padx=(20,20),  row=2, column=5)
    



# app
configWindow()
body()
root.mainloop()