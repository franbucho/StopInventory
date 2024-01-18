import tkinter as tk

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Inventario")

        self.inventario = Inventario()

        # Etiquetas y cajas de entrada
        self.label_producto = tk.Label(root, text="Producto:")
        self.entry_producto = tk.Entry(root)
        self.label_cantidad = tk.Label(root, text="Cantidad:")
        self.entry_cantidad = tk.Entry(root)

        # Botones
        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_producto)
        self.btn_sacar = tk.Button(root, text="Sacar", command=self.sacar_producto)
        self.btn_reporte = tk.Button(root, text="Generar Reporte", command=self.generar_reporte)

        # Pantalla para productos en stop
        self.label_stop = tk.Label(root, text="Productos en Stop:")
        self.text_stop = tk.Text(root, height=5, width=30, state=tk.DISABLED)

        # Diseño de la interfaz
        self.label_producto.grid(row=0, column=0)
        self.entry_producto.grid(row=0, column=1)
        self.label_cantidad.grid(row=1, column=0)
        self.entry_cantidad.grid(row=1, column=1)
        self.btn_agregar.grid(row=2, column=0, columnspan=2, pady=10)
        self.btn_sacar.grid(row=3, column=0, columnspan=2, pady=10)
        self.btn_reporte.grid(row=4, column=0, columnspan=2, pady=10)
        self.label_stop.grid(row=5, column=0, pady=10)
        self.text_stop.grid(row=6, column=0, columnspan=2, pady=10)

    def agregar_producto(self):
        producto = self.entry_producto.get()
        cantidad = int(self.entry_cantidad.get())
        self.inventario.agregar_producto(producto, cantidad)
        self.actualizar_interfaz()

    def sacar_producto(self):
        producto = self.entry_producto.get()
        cantidad = int(self.entry_cantidad.get())
        self.inventario.sacar_producto(producto, cantidad)
        self.actualizar_interfaz()

    def generar_reporte(self):
        # Obtener el reporte del inventario y actualizar la interfaz
        reporte = self.inventario.generar_reporte()
        self.text_stop.config(state=tk.NORMAL)
        self.text_stop.delete(1.0, tk.END)  # Limpiar el contenido anterior
        self.text_stop.insert(tk.END, reporte)
        self.text_stop.config(state=tk.DISABLED)

    def actualizar_interfaz(self):
        # Actualizar la pantalla de productos en stop
        productos_stop = self.inventario.obtener_productos_stop()
        self.text_stop.config(state=tk.NORMAL)
        self.text_stop.delete(1.0, tk.END)  # Limpiar el contenido anterior
        for producto in productos_stop:
            self.text_stop.insert(tk.END, f"{producto}\n")
        self.text_stop.config(state=tk.DISABLED)

class Inventario:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] += cantidad
        else:
            self.inventario[producto] = cantidad

    def sacar_producto(self, producto, cantidad):
        if producto in self.inventario:
            if self.inventario[producto] >= cantidad:
                self.inventario[producto] -= cantidad
            else:
                print(f"No hay suficiente cantidad de {producto} en inventario.")
        else:
            print(f"{producto} no está en inventario.")

    def generar_reporte(self):
        # Devolver el reporte como una cadena
        reporte = "Inventario actual:\n"
        for producto, cantidad in self.inventario.items():
            reporte += f"{producto}: {cantidad} unidades\n"
        return reporte

    def obtener_productos_stop(self):
        return [producto for producto, cantidad in self.inventario.items() if cantidad == 0]

# Configuración y ejecución de la interfaz
root = tk.Tk()
app = InventarioApp(root)
root.mainloop()
