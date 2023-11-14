from tkinter import *
from tkinter import messagebox
#hola desde mi mac

class Almacen:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def vender_producto(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] -= cantidad
            if self.productos[producto] == 0:
                del self.productos[producto]

    def mover_producto(self, destino, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] -= cantidad
            if self.productos[producto] == 0:
                del self.productos[producto]
            destino.agregar_producto(producto, cantidad)

    def visualizar_inventario(self):
        return f'{self.nombre}: {self.productos}'

# Crear almacenes
almacen1 = Almacen('almacen1')
almacen2 = Almacen('almacen2')

# Crear la ventana de la aplicación
global pantallaP  
pantallaP = Tk()
pantallaP.geometry("300x350")
pantallaP.title("TALLER ALGEBRA")       #Asignamos el titulo de la pantalla
Label(text = "INVENTARIO", bg = "blue", width = "300", height = "2", font = ("Verdana", 13), fg="white").pack() #Asignamos caracteristicas de la ventana
icono = PhotoImage(file="D:\PROYECTO ALGEBRA/icono.gif")
pantallaP.iconphoto(True, icono)

# Crear las entradas de texto para el nombre del producto y la cantidad
Label(text = "").pack()
Label(pantallaP, text = "Producto:").pack()
producto_entry = Entry(pantallaP)
producto_entry.pack()
Label(pantallaP, text = "Cantidad:").pack()
cantidad_entry = Entry(pantallaP)
cantidad_entry.pack()
agregar_button = Button(pantallaP, text="Agregar producto", command=lambda: almacen1.agregar_producto(producto_entry.get(), int(cantidad_entry.get())))  #BOTONES
vender_button = Button(pantallaP, text="Vender producto", command=lambda: almacen1.vender_producto(producto_entry.get(), int(cantidad_entry.get())))
mover_button = Button(pantallaP, text="Mover producto", command=lambda: almacen1.mover_producto(almacen2, producto_entry.get(), int(cantidad_entry.get())))
agregar_button.pack()
vender_button.pack()
mover_button.pack()

# Crear los botones para visualizar el inventario
Label(text = "").pack()
visualizar_button1 = Button(pantallaP, text="Visualizar inventario 1", command=lambda: messagebox.showinfo("Inventario 1", almacen1.visualizar_inventario()))
visualizar_button2 = Button(pantallaP, text="Visualizar inventario 2", command=lambda: messagebox.showinfo("Inventario 2", almacen2.visualizar_inventario()))
visualizar_button1.pack()
visualizar_button2.pack()

# Iniciar la aplicación
pantallaP.mainloop()
