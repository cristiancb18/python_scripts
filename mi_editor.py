from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from io import open 
import os

# Configuración de la raíz
root = Tk()
root.title("Editor de archivos de texto")
root.resizable(1,1)
menubar = Menu(root)
root.config(menu=menubar)
name = StringVar()
ruta = "" # La utilizaremos para almacenar la ruta del fichero
frame = None

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

# Listar todos los archivos en el directorio actual
archivos = os.listdir(directorio_actual)

# Filtrar solo los archivos .txt y guardarlos en una lista
archivos_txt = [archivo for archivo in archivos if archivo.endswith('.txt')]

#print (archivos_txt)


def crear():
    #convertir archivo a string
    nombre_archivo = name.get() 
    if nombre_archivo:
         nombre_archivo= nombre_archivo + ".txt"
         if nombre_archivo in archivos_txt:
             resultado = MessageBox.askquestion("Archivo existente","¿el archivo ya existe, está seguro que desea sobrescribirlo?")
             if resultado == "yes":  # "no"
    # Abre (o crea) un archivo llamado con el nombre que se puso y .txt en modo escritura ('w')
              with open(f"{nombre_archivo}", 'w') as archivo:
             # Escribe una línea de texto en el archivo
                  archivo.write('¡Hola, mundo!')
                  MessageBox.showinfo("Creacion de archivo","tu archivo se ha creado con exito")
         else:
              with open(f"{nombre_archivo}", 'w') as archivo:
             # Escribe una línea de texto en el archivo
                  archivo.write('¡Hola, mundo!')
                  MessageBox.showinfo("Creacion de archivo","tu archivo se ha creado con exito")
         entry.delete(0, END)    # Limpiar el Entry después de crear el archivo     


    else:
          MessageBox.showwarning("Advertencia", "Por favor, introduce un nombre para el archivo")
          
def mostrarnuevo():
    global frame
    global entry
    if frame:
        frame.destroy()  # Destruir el frame actual si existe
    #crea el cuadro de fondo para la interfaz de nuevo archivo
    frame = Frame(root, width=480, height=320)
    frame.pack(fill='both', expand=1)
    frame.config(cursor="arrow")
    frame.config(bg="lightblue")
    frame.config(bd=25)
    # Crear el Label como hijo del Frame
    label = Label(frame, text="Introduce el nombre que le quieres poner al archivo")
    label.pack(anchor="center")
    label.config(font=("Verdana",24))
    # Crear el segundo Label, Entry y Button como hijos del Frame
    label2 = Label(frame, text="Escribe el nombre del .txt aqui")
    label2.config(font=("Verdana",20))
    label2.pack(pady=10)
    #le decimos al entry que tome la variable global name
    entry = Entry(frame,textvariable=name)
    entry.config(font=("Verdana",20))
    entry.pack(pady=10)
    #aca le decimos al boton que llame la funcion crear
    button = Button(frame, text="Crear archivo", command=crear)
    button.pack(pady=10)
    button.config(font=("Verdana",24))
    #ajustar el tamaño de la ventana de acuerdo al contenido
    root.update_idletasks()
    root.geometry(f"{frame.winfo_width()}x{frame.winfo_height()}")


def abrir():
    global frame
    if frame:
        frame.destroy()  # Destruir el frame actual si existe
    global ruta
    global nombre_fichero
    ruta = FileDialog.askopenfilename(
		initialdir='.', 
		filetype=(("Ficheros de texto", "*.txt"),),
		title="Abrir un fichero de texto")
    nombre_fichero = os.path.basename(ruta)
    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        #print(contenido)
        #print(type(contenido))
#crea el cuadro de fondo para la interfaz de nuevo archivo
    frame = Frame(root, width=480, height=320)
    frame.pack(fill='both', expand=1)
    frame.config(cursor="arrow")
    frame.config(bg="lightgreen")
    frame.config(bd=25)
    # Crear el Label como hijo del Frame
    label = Label(frame, text=f"Aqui esta el contenido del archivo {nombre_fichero}:")
    label.pack(anchor="center")
    label.config(font=("Verdana",24))

        # Crear un Text para entrada de múltiples líneas
    text = Text(frame, height=10, width=40, wrap=WORD)
    text.pack(pady=10, side=LEFT, fill=BOTH, expand=True)
    text.insert(END, contenido)

    # Añadir barras de desplazamiento al Text
    scrollbar_y = Scrollbar(frame, orient=VERTICAL, command=text.yview)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    text.config(yscrollcommand=scrollbar_y.set)
    # Configurar el Text como solo lectura
    text.config(state=DISABLED)
    fichero.close()
    #print(ruta)
    #ajustar el tamaño de la ventana de acuerdo al contenido
    root.update_idletasks()
    root.geometry(f"{frame.winfo_width()}x{frame.winfo_height()}")



def modificar():
    
    #subfuncion de guardar el nuevo contenido
    def guardar():
        nuevo_contenido = text.get("1.0", END)  # Obtener el contenido actualizado del Text
        with open(ruta, 'w') as fichero:  # Abrir el archivo en modo escritura
           fichero.write(nuevo_contenido)
           fichero.close()
        MessageBox.showinfo("Modificacion de archivo","tu archivo se ha modificado correctamente")
        frame.destroy()
    
    
    global frame
    if frame:
        frame.destroy()  # Destruir el frame actual si existe
    global ruta
    #crea el cuadro de fondo para la interfaz de nuevo archivo
    frame = Frame(root, width=480, height=320)
    frame.pack(fill='both', expand=1)
    frame.config(cursor="arrow")
    frame.config(bg="lightpink")
    frame.config(bd=25)
    if ruta != "":
        fichero = open(ruta, 'r+')
        contenido = fichero.read()
        # Crear el Label como hijo del Frame
        label = Label(frame, text=f"modificando el archivo {nombre_fichero}:")
        label.pack(anchor="center")
        label.config(font=("Verdana",24))
        # Crear un Text para entrada de múltiples líneas
        text = Text(frame, height=10, width=40)
        text.pack(pady=10)
        text.insert(END, contenido)
        
        #insertamos el boton que llama la subfuncion guardar
        button = Button(frame, text="Guardar contenido", command=guardar)
        button.pack(pady=10)
        button.config(font=("Verdana",24))

    if ruta == "":
        MessageBox.showwarning("Advertencia", "Por favor primero abre un archivo antes de modificar")
        frame.destroy()
    
    #ajustar el tamaño de la ventana de acuerdo al contenido
    root.update_idletasks()
    root.geometry(f"{frame.winfo_width()}x{frame.winfo_height()}")
        
def guardarcomo():
    
    def guardarfinal():
        fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
        if fichero is not None:
            ruta = fichero.name
            nuevo_contenido = text.get("1.0", END)
            fichero = open(ruta, 'w+')
            fichero.write(nuevo_contenido)
            fichero.close()
            MessageBox.showinfo("Modificacion de archivo","tu archivo se ha guardado correctamente")
            frame.destroy()
        else:
            MessageBox.showerror("Error!","Ha ocurrido un error, guardado cancelado.")
            ruta = ""    
            
    global frame
    if frame:
        frame.destroy()  # Destruir el frame actual si existe
    global ruta

    #crea el cuadro de fondo para la interfaz de nuevo archivo
    frame = Frame(root, width=480, height=320)
    frame.pack(fill='both', expand=1)
    frame.config(cursor="arrow")
    frame.config(bg="lightcoral")
    frame.config(bd=25)
    label = Label(frame, text="Escribe el contenido del archivo aqui:")
    label.pack(anchor="center")
    label.config(font=("Verdana",24))
    # Crear un Text para entrada de múltiples líneas
    text = Text(frame, height=10, width=40)
    text.pack(pady=10)
 
    #insertamos el boton que llama la subfuncion guardar
    button = Button(frame, text="Guardar contenido", command=guardarfinal)
    button.pack(pady=10)
    button.config(font=("Verdana",24))          
    
    #ajustar el tamaño de la ventana de acuerdo al contenido
    root.update_idletasks()
    root.geometry(f"{frame.winfo_width()}x{frame.winfo_height()}")
        

#definicion del menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=mostrarnuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Modificar y guardar", command=modificar)
filemenu.add_command(label="Guardar como", command=guardarcomo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=filemenu)


# Finalmente bucle de la aplicación
root.mainloop()