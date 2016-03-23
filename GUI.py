import Tkinter as Tk
from Graph import graph as g

class GUI:
    def __init__(self):
        self.root = Tk.Tk()
        self.canvas = Tk.Canvas(self.root, width = 800, height = 800)
        self.add_node_button = Tk.Button(self.root, text='Add node')

        self.canvas.grid(row = 0, column = 0)
        self.add_node_button.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.graph = g()
        self.graph.load_romania_map()
        self.draw_romania_graph()

    def draw_romania_graph(self):
        for city in self.graph.cities:
            self.canvas.create_rectangle(city.x, city.y, city.x+10, city.y+10,outline=city.color)
            self.canvas.create_text(city.x-40, city.y+5, text=city.name, anchor=Tk.CENTER)
        for edge in self.graph.edges:
            city1 = self.graph.cities[edge[0]]
            city2 = self.graph.cities[edge[1]]
            self.canvas.create_line(city1.x+5, city1.y+5, city2.x+5, city2.y+5)


    def run(self):
        self.root.mainloop()