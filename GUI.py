import Tkinter as Tk
import tkMessageBox
from Graph import graph as g
import sys


class GUI:
    def __init__(self):
        self.root = Tk.Tk()

        self.result_string = Tk.StringVar(self.root)
        self.result_string.set('Result: ')
        self.canvas = Tk.Canvas(self.root, width = 800, height = 800)

        self.run_a_star_button = Tk.Button(self.root, text='A*', command=self.run_a_star)
        self.run_ucs_button = Tk.Button(self.root, text='Uniform Cost Search', command=self.run_ucs)
        self.run_gbfs_button= Tk.Button(self.root, text='Greedy Best First Search' , command= self.run_gbfs)
        self.result_label = Tk.Label(self.root, textvariable=self.result_string)
        self.canvas.grid(row = 0, column = 0, rowspan = 20)

        self.run_a_star_button.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.run_ucs_button.grid(row = 2, column = 1, padx = 5, pady = 5)
        self.run_gbfs_button.grid(row = 3 , column = 1,padx = 5, pady = 5)
        self.result_label.grid(row = 4, column = 1, padx = 5, pady = 5)

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
            self.root.after(700)
            end = self.graph.a_star_update()
            self.draw_romania_graph()
            self.canvas.update()
        self.result_string.set("Result: " + str(self.result()))

    def result(self):
        v = self.graph.g[self.graph.idx_goal]
        if v == sys.maxint:
            v = "Infinite Loop"
        elif v==-1:
            v = "NO path"
        return v
                    
    def call_ucs(self):
        self.graph.a_star_init()
        end = 0
        while end != -1:
            self.root.after(700)
            end = self.graph.ucs_update()
            self.draw_romania_graph()
            self.canvas.update()    
        self.result_string.set("Result: " + str(self.result()))

    def call_gbfs(self):
        self.graph.a_star_init()
        self.graph.g = [0 for i in range(self.graph.n)]
        self.graph.f = [0 for i in range(self.graph.n)]
        v = self.graph.idx_start
        self.graph.f[v] = 1
        self.graph.cities[v].color = 'Red'
        while True:
            end, check = self.graph.gbfs_update(v)
            v = end
            self.root.after(700)
            self.draw_romania_graph()
            self.canvas.update()
            if end == self.graph.idx_goal:
                print self.graph.g[end]
                break
            elif check == 1:
                print "Infinite loop"
                break
            elif check == 2:
                print "No Path"
                break
        self.result_string.set("Result: " + str(self.result()))

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
       
    def run_a_star(self):
        self.draw_romania_graph()
        self.call_a_star()
        self.draw_solution()
        self.graph.reset_color()
        
        
    def run_ucs(self):
        self.draw_romania_graph()
        self.call_ucs()
        self.draw_solution()
        self.graph.reset_color()       
    
    def run_gbfs(self):
        self.draw_romania_graph()
        self.call_gbfs()
        self.draw_solution()
        self.graph.reset_color()
        
    def run(self):
        self.root.mainloop()
         