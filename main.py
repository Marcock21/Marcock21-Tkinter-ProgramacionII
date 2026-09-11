import tkinter as tk
from crud import CRUDGenerico


def abrir_vehiculos():
    ventana_vehiculos = tk.Toplevel(ventana)

    campos = [
        "patente",
        "marca",
        "modelo"
    ]

    CRUDGenerico(
        ventana_vehiculos,
        "CRUD - Vehículos",
        campos
    )


def abrir_propietarios():
    ventana_propietarios = tk.Toplevel(ventana)

    campos = [
        "nombre",
        "apellido",
        "dni"
    ]

    CRUDGenerico(
        ventana_propietarios,
        "CRUD - Propietarios",
        campos
    )


ventana = tk.Tk()

ventana.title("Sistema de Gestión")
ventana.geometry("300x200")


titulo = tk.Label(
    ventana,
    text="Sistema de Gestión",
    font=("Arial", 16)
)

titulo.pack(pady=20)


boton_vehiculos = tk.Button(
    ventana,
    text="Vehículos",
    command=abrir_vehiculos
)

boton_vehiculos.pack(pady=5)


boton_propietarios = tk.Button(
    ventana,
    text="Propietarios",
    command=abrir_propietarios
)

boton_propietarios.pack(pady=5)


ventana.mainloop()