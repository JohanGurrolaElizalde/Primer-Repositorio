import tkinter as tk
from tkinter import Toplevel
ventanaprincipal=tk.Tk()
ventanaprincipal.title("Ventana principal")
ventanaprincipal.geometry("300x200")
def MOSTRAR_NOMBRE():
    ventana_nombre=Toplevel(ventanaprincipal)
    ventana_nombre.title("MIS DATOS")
    ventana_nombre.geometry("200x150")
    etiqueta=tk.Label(ventana_nombre,text="""Johan Gurrola Elizalde
    16 años bien vividos""",font=("Arial",10))
    etiqueta.pack(pady=10)
    boton_cerrar=tk.Button(ventana_nombre,text="CERRAR",command=ventana_nombre.destroy)
    boton_cerrar.pack(pady=10)
def Mostrar_MENSAJE ():
    ventana_mensaje=Toplevel(ventanaprincipal)
    ventana_mensaje.title("MENSAJE")
    ventana_mensaje.geometry("300x150")
    etiqueta2=tk.Label(ventana_mensaje,text="ESTE PROGRAMA FUE HECHO POR PYTHON",font=("Arial",10))
    etiqueta2.pack(pady=10)
    boton_cerrar2=tk.Button(ventana_mensaje,text="CERRAR",command=ventana_mensaje.destroy)
    boton_cerrar2.pack(pady=10)
boton_abrir=tk.Button(ventanaprincipal,text="Datos Creador",command=MOSTRAR_NOMBRE)
boton_abrir.pack(pady=10)
boton_abrir2=tk.Button(ventanaprincipal,text="MENSAJE",command=Mostrar_MENSAJE)
boton_abrir2.pack(pady=10)
ventanaprincipal.mainloop()
