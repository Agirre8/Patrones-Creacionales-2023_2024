# Archivo que define los ingredientes disponibles

class Ingrediente:
    def __init__(self, nombre, es_vegano=True):
        self.nombre = nombre
        self.es_vegano = es_vegano

class SalsaTomate(Ingrediente):
    pass

class Queso(Ingrediente):
    pass

class Topping(Ingrediente):
    pass

# Nuevos ingredientes para una pizza vegana
class Verdura(Ingrediente):
    pass

class SalsaVegana(Ingrediente):
    pass
