import tkinter as tk
from tkinter import ttk, messagebox


class CRUDGenerico:

    def __init__(self, ventana, titulo, campos):
        self.ventana = ventana
        self.titulo = titulo
        self.campos = campos

        self.registros = []
        self.entries = {}
        self.registro_seleccionado = None

        self.crear_interfaz()

    def crear_interfaz(self):

        self.ventana.title(self.titulo)

        # titulo
        titulo = tk.Label(
            self.ventana,
            text=self.titulo,
            font=("Arial", 16)
        )
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # crear los label y entry de forma dinamica

        for i, campo in enumerate(self.campos):

            label = tk.Label(
                self.ventana,
                text=campo.capitalize()
            )
            label.grid(row=i + 1, column=0, padx=10, pady=5)

            entry = tk.Entry(self.ventana)
            entry.grid(row=i + 1, column=1, padx=10, pady=5)

            self.entries[campo] = entry

        # botones
        fila_botones = len(self.campos) + 1

        tk.Button(
            self.ventana,
            text="Crear",
            command=self.crear
        ).grid(row=fila_botones, column=0, pady=10)

        tk.Button(
            self.ventana,
            text="Actualizar",
            command=self.actualizar
        ).grid(row=fila_botones, column=1, pady=10)

        tk.Button(
            self.ventana,
            text="Eliminar",
            command=self.eliminar
        ).grid(row=fila_botones, column=2, pady=10)

        # esta es la tabla
        self.tabla = ttk.Treeview(
            self.ventana,
            columns=self.campos,
            show="headings"
        )

        for campo in self.campos:
            self.tabla.heading(campo, text=campo.capitalize())
            self.tabla.column(campo, width=120)

        self.tabla.grid(
            row=fila_botones + 1,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )

        self.tabla.bind(
            "<ButtonRelease-1>",
            self.seleccionar_registro
        )

    def obtener_datos(self):

        datos = {}

        for campo, entry in self.entries.items():
            datos[campo] = entry.get()

        return datos

    def limpiar_campos(self):

        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def crear(self):

        datos = self.obtener_datos()

        #  aca valido loscampos vacíos
        for valor in datos.values():
            if valor.strip() == "":
                messagebox.showwarning(
                    "Campos vacíos",
                    "Todos los campos deben estar completos."
                )
                return

        self.registros.append(datos)

        self.mostrar_registros()
        self.limpiar_campos()

        messagebox.showinfo(
            "Éxito",
            "Registro creado correctamente."
        )

    def mostrar_registros(self):

        # limpiar la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # mostrar los registros
        for registro in self.registros:

            valores = []

            for campo in self.campos:
                valores.append(registro[campo])

            self.tabla.insert(
                "",
                tk.END,
                values=valores
            )

    def seleccionar_registro(self, evento):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        item = self.tabla.item(seleccion[0])
        valores = item["values"]

        self.registro_seleccionado = seleccion[0]

        for i, campo in enumerate(self.campos):

            self.entries[campo].delete(0, tk.END)
            self.entries[campo].insert(0, valores[i])

    def actualizar(self):

        if self.registro_seleccionado is None:
            messagebox.showwarning(
                "Sin selección",
                "Primero seleccioná un registro."
            )
            return

        datos = self.obtener_datos()

        for valor in datos.values():
            if valor.strip() == "":
                messagebox.showwarning(
                    "Campos vacíos",
                    "Todos los campos deben estar completos."
                )
                return

        indice = self.tabla.index(self.registro_seleccionado)

        self.registros[indice] = datos

        self.mostrar_registros()
        self.limpiar_campos()

        self.registro_seleccionado = None

        messagebox.showinfo(
            "Éxito",
            "Registro actualizado correctamente."
        )

    def eliminar(self):

        if self.registro_seleccionado is None:
            messagebox.showwarning(
                "Sin selección",
                "Primero seleccioná un registro."
            )
            return

        indice = self.tabla.index(self.registro_seleccionado)

        self.registros.pop(indice)

        self.mostrar_registros()
        self.limpiar_campos()

        self.registro_seleccionado = None

        messagebox.showinfo(
            "Éxito",
            "Registro eliminado correctamente."
        )