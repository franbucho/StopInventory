import json
import os
import tkinter as tk
from tkinter import messagebox

def registrar_usuario():
    username = entry_username.get()
    password = entry_password.get()

    # Verificar si el usuario ya existe
    usuarios = cargar_usuarios()
    if username in usuarios:
        messagebox.showinfo("Registro", "¡El usuario ya existe!")
        return

    # Registrar nuevo usuario
    usuarios[username] = {"password": password}
    guardar_usuarios(usuarios)
    messagebox.showinfo("Registro", "¡Registro exitoso!")

def autenticar_usuario():
    username = entry_username.get()
    password = entry_password.get()

    # Verificar si el usuario existe
    usuarios = cargar_usuarios()
    if username in usuarios and usuarios[username]["password"] == password:
        messagebox.showinfo("Autenticación", "¡Autenticación exitosa!")
        return

    messagebox.showinfo("Autenticación", "¡Error de autenticación!")

def cargar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Registro y Autenticación de Usuarios")

# Etiquetas y campos de entrada
label_username = tk.Label(root, text="Usuario:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Contraseña:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Botones de registro y autenticación
button_register = tk.Button(root, text="Registrar", command=registrar_usuario)
button_register.pack()

button_authenticate = tk.Button(root, text="Autenticar", command=autenticar_usuario)
button_authenticate.pack()

# Ejecutar la interfaz
root.mainloop()
