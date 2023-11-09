import tkinter as tk
from PizzaBuilder import Pizza, PizzaBuilder
from PizzaDirector import PizzaDirector
from Ingredientes import SalsaTomate, Queso, Topping, Verdura, SalsaVegana

class PizzaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Creador de Pizza")
        
        self.builder = PizzaBuilder([SalsaTomate(), Queso(), Topping(), Verdura(), SalsaVegana()])
        self.director = PizzaDirector()

        self.ingredientes_seleccionados = []

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Selecciona tus ingredientes:")
        self.label.pack()

        self.checkbox_vars = []
        for ingrediente in [SalsaTomate(), Queso(), Topping(), Verdura(), SalsaVegana()]:
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.frame, text=ingrediente.nombre, variable=var, command=lambda i=ingrediente: self.toggle_ingrediente(i, var))
            checkbox.pack()
            self.checkbox_vars.append(var)

        self.build_button = tk.Button(self.frame, text="Construir Pizza", command=self.construir_pizza)
        self.build_button.pack()

    def toggle_ingrediente(self, ingrediente, var):
        if var.get() == 1:
            self.ingredientes_seleccionados.append(ingrediente)
        else:
            self.ingredientes_seleccionados.remove(ingrediente)

    def construir_pizza(self):
        for ingrediente in self.ingredientes_seleccionados:
            self.builder.construir_ingrediente(ingrediente)
        
        self.director.construir_pizza(self.builder, es_vegana=False)  # Puedes cambiar es_vegana según el caso
        pizza_personalizada = self.builder.obtener_pizza()

        # Puedes imprimir los ingredientes seleccionados o realizar otras acciones
        print("Ingredientes seleccionados:", [ingrediente.nombre for ingrediente in self.ingredientes_seleccionados])

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaGUI(root)
    root.mainloop()

