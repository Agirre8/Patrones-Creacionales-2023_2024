
from Ingredientes import Ingrediente

class Pizza:
    def __init__(self):
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

class PizzaBuilder:
    def __init__(self, ingredientes_disponibles):
        self.pizza = Pizza()
        self.ingredientes_disponibles = ingredientes_disponibles

    def validar_ingrediente(self, ingrediente):
        return ingrediente in self.ingredientes_disponibles

    def construir_ingrediente(self, ingrediente):
        if self.validar_ingrediente(ingrediente):
            self.pizza.agregar_ingrediente(ingrediente)

    def obtener_pizza(self):
        return self.pizza
