import os
import subprocess
import webbrowser
import signal
import psutil
import platform
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as tb  # Importar ttkbootstrap correctamente
from PIL import Image, ImageTk  # Importar para manejar imágenes
# Variable para almacenar el proceso del servidor Flask
flask_process = None

# Función para instalar Python y los requisitos
def instalar_requerimientos():
    try:
        # Instalar los requerimientos desde el archivo requirements.txt
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        messagebox.showinfo("Instalación", "Requisitos instalados con éxito.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Hubo un problema al instalar los requisitos.")

# Función para iniciar el programa Flask
def iniciar_programa():
    global flask_process
    try:
        # Determinar el comando correcto para Python según el sistema operativo
        python_command = "python" if platform.system() == "Windows" else "python3"
        # Ejecutar el archivo Flask (app.py)
        flask_process = subprocess.Popen([python_command, "server.py"])
        webbrowser.open("http://127.0.0.1:8081/")  # Abrir el navegador en la dirección del servidor Flask
        messagebox.showinfo("Inicio", "Programa iniciado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al iniciar el programa: {str(e)}")

# Función para finalizar el programa Flask
def finalizar_programa():
    global flask_process
    try:
        if flask_process:
            # Terminar el proceso del servidor Flask
            flask_process.terminate()
            flask_process.wait()
            flask_process = None
            messagebox.showinfo("Finalizar", "Programa finalizado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "El programa no está en ejecución.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al finalizar el programa: {str(e)}")

# Crear la ventana principal con ttkbootstrap
ventana = tb.Window(themename="superhero")  # Se puede cambiar el tema (superhero, darkly, flatly, etc.)
ventana.title("Programa Administrador")
ventana.geometry("300x200")

# Crear un marco para organizar los botones
frame = tb.Frame(ventana)
frame.pack(pady=20, padx=20)

# Cargar imágenes para los botones
instalar_icon = ImageTk.PhotoImage(Image.open("img/descargar.png").resize((20, 20)))  # Ajustar el tamaño según sea necesario
iniciar_icon = ImageTk.PhotoImage(Image.open("img/start.png").resize((20, 20)))
finalizar_icon = ImageTk.PhotoImage(Image.open("img/salida.png").resize((20, 20)))

# Botones para las acciones utilizando ttkbootstrap
btn_instalar = tb.Button(frame, text="Instalar", bootstyle="primary", command=instalar_requerimientos, width=20, image=instalar_icon, compound='left')
btn_instalar.pack(pady=10)

btn_iniciar = tb.Button(frame, text="Iniciar Programa", bootstyle="success", command=iniciar_programa, width=20, image=iniciar_icon, compound='left')
btn_iniciar.pack(pady=10)

btn_finalizar = tb.Button(frame, text="Finalizar Programa", bootstyle="danger", command=finalizar_programa, width=20, image=finalizar_icon, compound='left')
btn_finalizar.pack(pady=10)

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()
