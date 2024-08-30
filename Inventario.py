import tkinter as tk
from tkinter import ttk
import re
from datetime import datetime
from tkinter import simpledialog


# Función para dar formato a la fecha mientras el usuario la ingresa
def formatear_fecha(event):
    entrada = fecha_entry.get()
    longitud = len(entrada)

    if event.keysym == "BackSpace" or longitud == 2 or longitud == 5:
        fecha_entry.insert(tk.END, '/')
    elif longitud == 11:
        fecha_entry.delete(10, tk.END)


# Función para agregar un libro al inventario
def agregar_libro():
    categoria = categoria_var.get()
    genero = genero_var.get()
    fecha = fecha_entry.get()

    # Verificar si la fecha cumple con el formato "dd/mm/aaaa" usando expresiones regulares
    if not re.match(r"\d{2}/\d{2}/\d{4}", fecha):
        tk.messagebox.showerror("Error", "El formato de fecha debe ser  dia, mes y año 'dd/mm/aaaa'.")
        return

    # Verificar si la fecha es válida utilizando el módulo datetime
    try:
        datetime.strptime(fecha, '%d/%m/%Y')
    except ValueError:
        tk.messagebox.showerror("Error", "La fecha ingresada no es válida.")
        return

    monto = float(monto_entry.get())

    libro = {
        "Categoría": categoria,
        "Género": genero,
        "Fecha": fecha,
        "Monto": monto
    }
    inventario.append(libro)
    actualizar_lista()
    limpiar_campos()


# Función para editar la categoría, el género y el monto de un libro
def editar_libro():
    libro_index = libros_disponibles.curselection()
    if len(libro_index) == 0:
        tk.messagebox.showerror("Error", "Seleccione un libro del inventario para editarlo.")
        return

    libro_index = libro_index[0]
    nuevo_categoria = simpledialog.askstring("Editar Categoría", "Ingrese la nueva categoría:")
    nuevo_genero = simpledialog.askstring("Editar Género", "Ingrese el nuevo género:")
    nuevo_monto = simpledialog.askfloat("Editar Monto", "Ingrese el nuevo monto:")

    if nuevo_categoria is not None:
        inventario[libro_index]["Categoría"] = nuevo_categoria
    if nuevo_genero is not None:
        inventario[libro_index]["Género"] = nuevo_genero
    if nuevo_monto is not None:
        inventario[libro_index]["Monto"] = nuevo_monto

    actualizar_lista()
    mostrar_inventario()


# Función para mostrar la lista de libros en el inventario
def mostrar_inventario():
    libros_disponibles.delete(0, tk.END)
    for i, libro in enumerate(inventario, start=1):
        libros_disponibles.insert(tk.END,
                                  f"Libro #{i}: {libro['Categoría']}, Género: {libro['Género']}, Monto: ${libro['Monto']:.2f}")


# Función para actualizar la lista de libros en la interfaz
def actualizar_lista():
    lista_text.delete(1.0, tk.END)
    for i, libro in enumerate(inventario, start=1):
        lista_text.insert(tk.END, f"Libro #{i}\n")
        lista_text.insert(tk.END, f"Categoría: {libro['Categoría']}\n")
        lista_text.insert(tk.END, f"Género: {libro['Género']}\n")
        lista_text.insert(tk.END, f"Fecha: {libro['Fecha']}\n")
        lista_text.insert(tk.END, f"Monto: ${libro['Monto']:.2f}\n")
        lista_text.insert(tk.END, "-----------\n")


# Función para limpiar los campos de entrada
def limpiar_campos():
    categoria_var.set(categorias[0])
    genero_var.set(generos[0])  # Inicializa con el primer género
    fecha_entry.delete(0, tk.END)
    monto_entry.delete(0, tk.END)


# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Inventario de Libros")

# Crear un Menú desplegable para seleccionar la categoría
categorias = ["Ingenieria", "Literatura", "Administración", "Matematica"]
categoria_frame = ttk.LabelFrame(root, text="Categoría")
categoria_frame.pack(padx=10, pady=10, fill="x")
categoria_var = tk.StringVar(value=categorias[0])
categoria_menu = ttk.Combobox(categoria_frame, textvariable=categoria_var, values=categorias)
categoria_menu.pack(fill="x", expand=True)

# Lista de géneros
generos = ["Femenino", "Masculino"]
genero_frame = ttk.LabelFrame(root, text="Género")
genero_frame.pack(padx=10, pady=10, fill="x")
genero_var = tk.StringVar(value=generos[0])  # Inicializa con el primer género
genero_radiobutton_femenino = ttk.Radiobutton(genero_frame, text="Femenino", variable=genero_var, value="Femenino")
genero_radiobutton_masculino = ttk.Radiobutton(genero_frame, text="Masculino", variable=genero_var, value="Masculino")
genero_radiobutton_femenino.pack(fill="x", expand=True)
genero_radiobutton_masculino.pack(fill="x", expand=True)

# Crear un campo de entrada para ingresar la fecha en formato "dd/mm/aaaa"
fecha_frame = ttk.LabelFrame(root, text="Fecha de adquisición (dd/mm/aaaa)")
fecha_frame.pack(padx=10, pady=10, fill="x")
fecha_entry = ttk.Entry(fecha_frame)
fecha_entry.pack(fill="x", expand=True)
fecha_entry.bind("<KeyRelease>", formatear_fecha)

# Crear un campo de entrada para el monto
monto_frame = ttk.LabelFrame(root, text="Monto")
monto_frame.pack(padx=10, pady=10, fill="x")
monto_entry = ttk.Entry(monto_frame)
monto_entry.pack(fill="x", expand=True)

# Botón para agregar un libro
agregar_button = ttk.Button(root, text="Agregar Libro", command=agregar_libro)
agregar_button.pack(pady=10, padx=10, fill="x")

# Lista de libros disponibles en el inventario
inventario_frame = ttk.LabelFrame(root, text="Inventario de Libros")
inventario_frame.pack(padx=10, pady=10, fill="both", expand=True)
libros_disponibles = tk.Listbox(inventario_frame, selectmode=tk.SINGLE)
libros_disponibles.pack(fill="both", expand=True)

# Botón para mostrar la lista de libros disponibles en el inventario
mostrar_inventario_button = ttk.Button(inventario_frame, text="Mostrar Inventario", command=mostrar_inventario)
mostrar_inventario_button.pack(pady=10, fill="x", expand=True)

# Botón para editar el libro seleccionado
editar_libro_button = ttk.Button(inventario_frame, text="Editar Libro", command=editar_libro)
editar_libro_button.pack(pady=10, fill="x", expand=True)

# Crear un área de texto para mostrar la lista de libros
lista_text = tk.Text(root, height=10, width=40)
lista_text.pack(padx=10, pady=10, fill="both", expand=True)

# Crear una lista para almacenar los libros
inventario = []

root.mainloop()
