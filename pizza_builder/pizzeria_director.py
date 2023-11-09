# pizzeria_director.py

from pizza_builder import PizzaBuilder

class PizzeriaDirector:
    def construir_pizza(self, builder: PizzaBuilder):
        builder.construir_masa()
        builder.construir_salsa()
        builder.construir_ingredientes()
        return builder.obtener_pizza()
