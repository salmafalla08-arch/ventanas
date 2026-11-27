import tkinter as tk  # Importar las herramientas gráficas  y le asigna el alias tk

ventana = tk.Tk()  # Crear una sola ventana raíz
ventana.title("Mi primera ventana")  # Texto de la barra de título
ventana.geometry("400x220")  # Ancho de 400 y alto de 220 píxeles
ventana.resizable(True, False)  # Permitir cambiar el ancho, no el alto
ventana.mainloop()  # Atender clics y redibujados hasta cerrar
