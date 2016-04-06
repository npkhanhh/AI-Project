import Tkinter as Tk
from Graph import graph as g


class GUI:
    def __init__(self):
        self.root = Tk.Tk()
        self.algorithm_option = ["Uniform Cost Search", "A*", "Greedy Best First Search"]
        self.algorithm_var = Tk.StringVar(self.root)
        self.algorithm_var.set(self.algorithm_option[0])

        self.canvas = Tk.Canvas(self.root, width = 800, height = 800)
        self.add_node_button = Tk.Button(self.root, text='Add node')
        self.algorithm_menu = apply(Tk.OptionMenu, (self.root, self.algorithm_var) + tuple(self.algorithm_option))
        self.run_algorithm_button = Tk.Button(self.root, text='Run algorithm', command=self.run_a_star)

        self.canvas.grid(row = 0, column = 0, rowspan = 20)
        self.add_node_button.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.algorithm_menu.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.run_algorithm_button.grid(row = 2, column = 1, padx = 5, pady = 5)


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
            self.canvas.create_text((city1.x+city2.x)/2+10, (city1.y+city2.y)/2-10, text = edge[2])

    def call_a_star(self):
        self.graph.a_star_init()
        end = 0
        while end != -1:
            self.root.after(600)
            end = self.graph.a_star_update()
            self.draw_romania_graph()
            self.canvas.update()


    def draw_solution(self):
        u = self.graph.idx_goal
        while True:
            i=self.graph.trace[u]
            self.graph.cities[u].color='yellow'
            self.graph.cities[i].color='yellow'
            city1= self.graph.cities[u]
            city2= self.graph.cities[i]
            self.canvas.create_line(city1.x+5,city1.y+5,city2.x+5,city2.y+5,fill='yellow')
            u = i
            if i == self.graph.idx_start:
                break
        #self.canvas.update()

    def run_a_star(self):
        self.draw_romania_graph()
        self.call_a_star()
        self.draw_solution()
        self.graph.reset_color()




    def run(self):
        self.root.mainloop()