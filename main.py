# 1. Interfaz del Producto (Pizza)
class Pizza:
    def __init__(self): 
        self.masa = None
        self.salsa = None
        self.ingredientes = []

    def __str__(self):
        return f"Masa: {self.masa}, Salsa: {self.salsa}, Ingredientes: {', '.join(self.ingredientes)}"


# 2. Interfaz del Constructor (PizzaBuilder)
from abc import ABC, abstractmethod

class PizzaBuilder(ABC):
    @abstractmethod
    def construir_masa(self):
        pass

    @abstractmethod
    def construir_salsa(self):
        pass

    @abstractmethod
    def construir_ingredientes(self):
        pass

    def obtener_pizza(self):
        pass


# 3. Constructores Concretos (PizzaBuilderConcreto)
class PizzaMargheritaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def construir_masa(self):
        self.pizza.masa = "Masa delgada"

    def construir_salsa(self):
        self.pizza.salsa = "Salsa clásica de tomate"

    def construir_ingredientes(self):
        self.pizza.ingredientes.append("Queso mozzarella")
        self.pizza.ingredientes.append("Albahaca fresca")

    def obtener_pizza(self):
        return self.pizza


class PizzaPremiumBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def construir_masa(self):
        self.pizza.masa = "Masa fermentada por 48 horas"

    def construir_salsa(self):
        self.pizza.salsa = "Salsa de autor"

    def construir_ingredientes(self):
        self.pizza.ingredientes.append("Ingredientes especiales")

    def obtener_pizza(self):
        return self.pizza

# 4. Director (PizzeriaDirector)
class PizzeriaDirector:
    def construir_pizza(self, builder):
        builder.construir_masa()
        builder.construir_salsa()
        builder.construir_ingredientes()
        return builder.obtener_pizza()


# 5. Cliente
if __name__ == "__main__":
    director = PizzeriaDirector()

    margherita_builder = PizzaMargheritaBuilder()
    pizza_margherita = director.construir_pizza(margherita_builder)
    print("Pizza Margherita:", pizza_margherita)

    premium_builder = PizzaPremiumBuilder()
    pizza_premium = director.construir_pizza(premium_builder)
    print("Pizza Premium:", pizza_premium)

import tkinter as tk

class PizzaBuilderGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Creador de Pizza")

        self.pizza = Pizza()  # Creamos una pizza en blanco
        self.ingredientes_seleccionados = []

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Selecciona tus ingredientes:")
        self.label.pack()

        self.checkbox_vars = []

        # Agrega ingredientes a la pizza personalizada
        for ingrediente in ["Masa delgada", "Salsa clásica", "Queso", "Pepperoni", "Champiñones", "Aceitunas"]:
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
        if var.get() == 1:
            self.ingredientes_seleccionados.append(ingrediente)
        else:
            self.ingredientes_seleccionados.remove(ingrediente)

    def construir_pizza(self):
        print("Pizza personalizada construida:")
        print("Ingredientes:", self.ingredientes_seleccionados)

        # Mostrar ingredientes seleccionados en la interfaz
        self.result_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
        for ingrediente in self.ingredientes_seleccionados:
            self.result_text.insert(tk.END, ingrediente + "\n")
        self.result_text.config(state=tk.DISABLED)  # Deshabilitar la edición


class Pizza:
    def __init__(self):
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
