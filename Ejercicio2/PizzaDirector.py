import tkinter as tk
from PizzaBuilder import PizzaBuilder

class PizzaGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Pizza Builder")
        self.pizza_builder = PizzaBuilder()

        # Aquí puedes añadir tus widgets de interfaz gráfica

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaGUI(root)
    root.mainloop()