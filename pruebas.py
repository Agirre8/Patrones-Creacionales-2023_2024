import tkinter as tk

class PizzaBuilderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Creador de Pizza")

        self.pizza = Pizza()  # Creamos una pizza en blanco
        self.ingredientes_seleccionados = []
        self.tipo_masa = tk.StringVar(value="Masa delgada")  # Valor por defecto: masa delgada
        self.tipo_salsa = tk.StringVar(value="Salsa clásica")  # Valor por defecto: salsa clásica

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        # Agrega opciones para elegir el tipo de masa
        self.label_masa = tk.Label(self.frame, text="Selecciona el tipo de masa:")
        self.label_masa.pack()

        self.radio_masa_delgada = tk.Radiobutton(self.frame, text="Masa delgada", variable=self.tipo_masa, value="Masa delgada")
        self.radio_masa_delgada.pack()

        self.radio_masa_normal = tk.Radiobutton(self.frame, text="Masa normal", variable=self.tipo_masa, value="Masa normal")
        self.radio_masa_normal.pack()

        # Agrega opciones para elegir el tipo de salsa
        self.label_salsa = tk.Label(self.frame, text="Selecciona el tipo de salsa:")
        self.label_salsa.pack()

        self.radio_salsa_normal = tk.Radiobutton(self.frame, text="Salsa clásica", variable=self.tipo_salsa, value="Salsa clásica")
        self.radio_salsa_normal.pack()

        self.radio_salsa_barbacoa = tk.Radiobutton(self.frame, text="Salsa barbacoa", variable=self.tipo_salsa, value="Salsa barbacoa")
        self.radio_salsa_barbacoa.pack()

        self.radio_salsa_carbonara = tk.Radiobutton(self.frame, text="Salsa carbonara", variable=self.tipo_salsa, value="Salsa carbonara")
        self.radio_salsa_carbonara.pack()

        self.label_ingredientes = tk.Label(self.frame, text="Selecciona tus ingredientes (máximo 5):")
        self.label_ingredientes.pack()

        self.checkbox_vars = []

        # Agrega ingredientes a la pizza personalizada
        ingredientes_disponibles = ["Queso", "Pepperoni", "Champiñones", "Aceitunas",
                                    "York", "Bacon", "Cebolla", "Pimiento", "Carne"]
        for ingrediente in ingredientes_disponibles:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.frame, text=ingrediente, variable=var, command=lambda i=ingrediente, v=var: self.toggle_ingrediente(i, v))
            checkbox.pack()
            self.checkbox_vars.append(var)

        self.build_button = tk.Button(self.frame, text="Construir Pizza", command=self.construir_pizza)
        self.build_button.pack()

        self.result_label = tk.Label(self.frame, text="Ingredientes seleccionados:")
        self.result_label.pack()

        self.result_text = tk.Text(self.frame, height=5, width=40)
        self.result_text.pack()

    def toggle_ingrediente(self, ingrediente, var):
        # Verificar la restricción de un máximo de 5 ingredientes
        if var.get() == 1 and len(self.ingredientes_seleccionados) < 5:
            self.ingredientes_seleccionados.append(ingrediente)
        elif var.get() == 0 and ingrediente in self.ingredientes_seleccionados:
            self.ingredientes_seleccionados.remove(ingrediente)

    def construir_pizza(self):
        # Crear la pizza con los ingredientes seleccionados, el tipo de masa y el tipo de salsa
        self.pizza = Pizza()
        self.pizza.tipo_masa = self.tipo_masa.get()
        self.pizza.tipo_salsa = self.tipo_salsa.get()
        for ingrediente in self.ingredientes_seleccionados:
            self.pizza.agregar_ingrediente(ingrediente)

        # Mostrar la información en la interfaz
        print("Pizza personalizada construida:")
        print("Tipo de masa:", self.pizza.tipo_masa)
        print("Tipo de salsa:", self.pizza.tipo_salsa)
        print("Ingredientes:", self.pizza.ingredientes)

        self.result_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
        self.result_text.insert(tk.END, f"Tipo de masa: {self.pizza.tipo_masa}\n")
        self.result_text.insert(tk.END, f"Tipo de salsa: {self.pizza.tipo_salsa}\n")
        for ingrediente in self.pizza.ingredientes:
            self.result_text.insert(tk.END, ingrediente + "\n")
        self.result_text.config(state=tk.DISABLED)  # Deshabilitar la edición


class Pizza:
    def __init__(self):
        self.tipo_masa = None
        self.tipo_salsa = None
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def remover_ingrediente(self, ingrediente):
        if ingrediente in self.ingredientes:
            self.ingredientes.remove(ingrediente)


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaBuilderGUI(root)
    root.mainloop()
