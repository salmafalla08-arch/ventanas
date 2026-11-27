import tkinter as tk # Importa la librería tkinter y le asigna el alias tk
from tkinter import messagebox, ttk # Importa messagebox y ttk desde tkinter para cuadros de diálogo y widgets temáticos

# Crear la ventana principal
ventana = tk.Tk() #crea la ventana principal de la aplicación.
ventana.title("Mi primera aplicación")
ventana.geometry("350x200") # Define tamaño y posición inicial de la ventana


def saludar():
    messagebox.showinfo("Saludo", "¡Bienvenido a Python!") #muestra un mensaje emergente cuando el usuario presiona el botón.

# crea una etiqueta que muestra un texto.
etiqueta = ttk.Label(
    ventana,
    text="Aprendiendo Tkinter"
)
etiqueta.pack(pady=20)

# crea un botón interactivo.
boton = ttk.Button(
    ventana,
    text="Saludar",
    command=saludar #relaciona el botón con la función saludar.
)
boton.pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop() #inicia el ciclo de eventos para que la aplicación responda a las interacciones del usuario.