# pizza.py

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

    def __str__(self):
        return f"Tipo de masa: {self.tipo_masa}, Tipo de salsa: {self.tipo_salsa}, Ingredientes: {', '.join(self.ingredientes)}"
