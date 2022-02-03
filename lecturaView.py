import tkinter as tk
from tkinter import ttk
from tkinter import *


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
    ancho_ventana = 600
    alto_ventana = 150

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)

    root.geometry(posicion)
    root.resizable(0, 0)

    #root.rowconfigure(0, weight=1)

    root.columnconfigure(1, weight=2)
    root.columnconfigure(3, weight=2)
    root.columnconfigure(5, weight=2)



#configuracion pantalla 2
def configWindow2(idPrueba):
    #tamaño y pos de pantalla
    pantallaResultado = Toplevel()
    
    pantallaResultado.title("Resultados")
    ancho_ventana = 600
    alto_ventana = 150

    x_ventana = pantallaResultado.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = pantallaResultado.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana+10) + "+" + str(y_ventana+10)

    pantallaResultado.geometry(posicion)
    pantallaResultado.resizable(0, 0)
    IdPrueba = tk.Label(pantallaResultado, text=idPrueba)
    IdPrueba.grid(pady=(30,5), padx=5, row=0, column=0)
    

 



#obtencion de datos
def obtenerParametros():
    idPrueba = idPruebaEntry.get()
    ant = antEntry.get()
    metraje = metajeCombo.get()
    tag1 = tagEntry1.get()
    tag2 = tagEntry2.get()
    tag3 = tagEntry3.get()
    segundo = segCombo.get()

    print(idPrueba + ant + metraje + tag1 + tag2 + tag3 + segundo)
    configWindow2(idPrueba)
    


#widgets 

#variables


#variables set
segundosLista = ['60', '120', '180','240','300']
segundoSet = tk.StringVar(root)
segundoSet.set('60')

metrajeLista = ['160','150','140','130','120','110','100','90','80','70','60','50','40','30','20','10','0','-10','-20','-30','-40','-50','-60','-70','-80','-90','-100','110','-120','-130','-140','-150','-160']
metrajeSet = tk.StringVar(root)
metrajeSet.set('160')

# Crear caja de texto.
idPruebaEntry = tk.Entry(root)
antEntry = tk.Entry(root)
metajeCombo =  ttk.Combobox(root,values = metrajeLista)
segCombo = ttk.Combobox(root,values = segundosLista)
tagEntry1 = tk.Entry(root)
tagEntry2 = tk.Entry(root)
tagEntry3 = tk.Entry(root)

#botones
lecturaBtn= tk.Button(root, text="Ejecutar Lectura",bg="#3498DB", fg="white", command = obtenerParametros)




# Posicionarla en la ventana.
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