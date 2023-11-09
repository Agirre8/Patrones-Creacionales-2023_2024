from typing import List

# Producto: Pizza
class Pizza:
    def __init__(self):
        self.tipo_masa = None
        self.salsa_base = None
        self.ingredientes_principales = []

    def __str__(self):
        return f"Pizza con {self.tipo_masa} y {', '.join(self.ingredientes_principales)}"

# Interfaz Builder: PizzaBuilder
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build_tipo_masa(self):
        pass

    def build_salsa_base(self):
        pass

    def build_ingredientes_principales(self):
        pass

    # ... otros métodos de construcción ...

# Concrete Builder 1: PizzaBuilderClasica
class PizzaBuilderClasica(PizzaBuilder):
    def build_tipo_masa(self):
        self.pizza.tipo_masa = "Masa Clásica"

    def build_salsa_base(self):
        self.pizza.salsa_base = "Salsa de Tomate"

    def build_ingredientes_principales(self):
        self.pizza.ingredientes_principales = ["Queso", "Pepperoni"]

# Concrete Builder 2: PizzaBuilderVegana
class PizzaBuilderVegana(PizzaBuilder):
    def build_tipo_masa(self):
        self.pizza.tipo_masa = "Masa Vegana"

    def build_salsa_base(self):
        self.pizza.salsa_base = "Salsa de Tomate Vegana"

    def build_ingredientes_principales(self):
        self.pizza.ingredientes_principales = ["Tomate", "Aceitunas", "Champiñones"]

# Director: PizzaDirector
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_tipo_masa()
        self.builder.build_salsa_base()
        self.builder.build_ingredientes_principales()
        # ... otros pasos de construcción ...

    def get_pizza(self):
        return self.builder.pizza

# Cliente
def main():
    builder_clasica = PizzaBuilderClasica()
    director_clasica = PizzaDirector(builder_clasica)
    director_clasica.construct_pizza()
    pizza_clasica = director_clasica.get_pizza()
    print("Pizza Clásica:", pizza_clasica)

    builder_vegana = PizzaBuilderVegana()
    director_vegana = PizzaDirector(builder_vegana)
    director_vegana.construct_pizza()
    pizza_vegana = director_vegana.get_pizza()
    print("Pizza Vegana:", pizza_vegana)

if __name__ == "__main__":
    main()
