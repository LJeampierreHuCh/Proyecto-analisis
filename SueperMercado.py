from tkinter import *
from tkinter import messagebox

# Lista para almacenar los clientes
clientes = []


def agregar_cliente():
    nombre = entry_nombre.get()
    ticket = entry_ticket.get()
    edad = entry_edad.get()
    genero = entry_genero.get()

    # Validar que la edad sea un número
    try:
        edad = int(edad)
    except ValueError:
        messagebox.showerror("Error", "La edad debe ser un número.")
        return

    if nombre and ticket and edad and genero:
        # Agregar el cliente a la lista
        clientes.append((nombre, ticket, edad, genero))
        # Limpiar campos
        entry_nombre.delete(0, END)
        entry_ticket.delete(0, END)
        entry_edad.delete(0, END)
        entry_genero.delete(0, END)
        # Actualizar la lista de clientes
        actualizar_lista()
    else:
        messagebox.showerror("Error", "Por favor complete todos los campos.")


def actualizar_lista():
    # Ordenar la lista de clientes
    clientes.sort(key=prioridad_cliente)
    # Limpiar el cuadro de lista
    lista_clientes.delete(0, END)
    # Agregar los clientes a la lista
    for cliente in clientes:
        lista_clientes.insert(END, f"{cliente[0]} (Ticket: {cliente[1]}, Edad: {cliente[2]}, Género: {cliente[3]})")


def prioridad_cliente(cliente):
    nombre, ticket, edad, genero = cliente
    # Definir prioridades
    if edad >= 65:
        return (0,)  # Mayor de 65 años
    if genero.lower() == "f" and "embarazada" in nombre.lower():  # Suponiendo que el nombre contiene "embarazada"
        return (1,)  # Mujer embarazada
    return (2,)  # Otros (mujeres y hombres)


# Configuración de la ventana
window = Tk()
window.title("Gestor de filas en un SuperMercado")
window.geometry("500x500")

# Centrar la ventana en la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = 500
window_height = 500
x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Configuración de las filas y columnas
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(6, weight=1)

# Logo
canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file="Iconosuper.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=2)

# Entradas de datos
Label(window, text="Nombre:").grid(column=0, row=1, sticky="e")
entry_nombre = Entry(window)
entry_nombre.grid(column=1, row=1, sticky="w")

Label(window, text="Número de Ticket:").grid(column=0, row=2, sticky="e")
entry_ticket = Entry(window)
entry_ticket.grid(column=1, row=2, sticky="w")

Label(window, text="Edad:").grid(column=0, row=3, sticky="e")
entry_edad = Entry(window)
entry_edad.grid(column=1, row=3, sticky="w")

Label(window, text="Género (M/F):").grid(column=0, row=4, sticky="e")
entry_genero = Entry(window)
entry_genero.grid(column=1, row=4, sticky="w")

# Botón para agregar cliente
boton_agregar = Button(window, text="Agregar Cliente", command=agregar_cliente)
boton_agregar.grid(column=0, row=5, columnspan=2)

# Lista para mostrar clientes
lista_clientes = Listbox(window, width=50)
lista_clientes.grid(column=0, row=6, columnspan=2, pady=10)

window.mainloop()