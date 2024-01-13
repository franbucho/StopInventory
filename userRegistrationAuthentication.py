import json
import os

def registrar_usuario(username, password):
    # Verificar si el usuario ya existe
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)
            if username in usuarios:
                print("¡El usuario ya existe!")
                return False

    # Registrar nuevo usuario
    with open("usuarios.json", "a+") as file:
        usuarios = json.load(file) if os.path.exists("usuarios.json") else {}
        usuarios[username] = {"password": password}
        file.seek(0)
        json.dump(usuarios, file)
        print("¡Registro exitoso!")
        return True

def autenticar_usuario(username, password):
    # Verificar si el usuario existe
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as file:
            usuarios = json.load(file)
            if username in usuarios and usuarios[username]["password"] == password:
                print("¡Autenticación exitosa!")
                return True

    print("¡Error de autenticación!")
    return False

# Ejemplo de registro de usuario
registrar_usuario("usuario1", "contrasena123")

# Ejemplo de autenticación de usuario
autenticar_usuario("usuario1", "contrasena123")
