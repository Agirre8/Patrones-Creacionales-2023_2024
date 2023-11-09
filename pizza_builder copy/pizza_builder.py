# pizza_builder.py

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

class PizzaMargheritaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def construir_masa(self):
        self.pizza.tipo_masa = "Masa delgada"

    def construir_salsa(self):
        self.pizza.tipo_salsa = "Salsa clásica"

    def construir_ingredientes(self):
        self.pizza.ingredientes.append("Queso")
        self.pizza.ingredientes.append("Albahaca")

    def obtener_pizza(self):
        return self.pizza

class PizzaPremiumBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def construir_masa(self):
        self.pizza.tipo_masa = "Masa fermentada por 48 horas"

    def construir_salsa(self):
        self.pizza.tipo_salsa = "Salsa de autor"

    def construir_ingredientes(self):
        self.pizza.ingredientes.append("Ingredientes especiales")

    def obtener_pizza(self):
        return self.pizza
