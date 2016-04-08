#import networkx as nw
import sys
class city:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
        self.color = 'black'

class graph:
    def __init__(self):
        self.cities = []
        self.a = []
        self.edges = []
        self.dict = {}
        self.start = None
        self.goal = None
        self.h = []
        self.n = 0
        self.m = 0
        self.trace = []

    def load_romania_map(self):
        f = open('romania_map.txt', 'r')
        [self.n, self.m] = map(int, f.readline().split())
        for i in range(self.n):
            c = f.readline().split()
            self.cities.append(city(c[0], int(c[1]), int(c[2])))
            self.dict[c[0]] = i

        self.a = [[0 for i in self.cities] for j in self.cities]

        for i in range(self.m):
            edge = f.readline().split()
            idx1, idx2 = self.dict[edge[0]], self.dict[edge[2]]
            weight = int(edge[1])
            self.a[idx1][idx2] = weight
            self.edges.append([idx1, idx2, weight])
        self.h = [0 for i in self.cities]
        f.close()
        self.heuristic_input()

    def heuristic_input(self):
        f = open('heuristic_romania_map.txt', 'r')
        [self.start, self.goal] = f.readline().split()
        self.idx_start = self.dict[self.start]
        self.idx_goal = self.dict[self.goal]
        while True:
            s = f.readline().split()
            if not s:
                break
            idx = self.dict[s[0]]
            self.h[idx] = int(s[1])
        f.close()

    def a_star_init(self):
        self.f = [sys.maxint for i in range(self.n)]
        self.g = [sys.maxint for i in range(self.n)]
        self.g[self.idx_start] = 0
        self.f[self.idx_start] = self.h[self.idx_start]
        self.closed = [False for i in range(self.n)]
        self.trace = [0 for i in range(self.n)]

    def a_star_update(self):

        u = -1
        min = sys.maxint
        for i in range(self.n):
            if not self.closed[i] and self.f[i] < min:
                min = self.f[i]
                u = i
        self.closed[u] = True
        self.cities[u].color = 'red'
        if u == self.idx_goal or u == -1:
            return -1

        for i in range(self.n):
            if self.a[u][i] != 0 and self.g[i] > self.g[u] + self.a[u][i]:
                self.g[i] = self.g[u] + self.a[u][i]
                self.f[i] = self.g[i] + self.h[i]
                self.cities[i].color = 'green'
                self.trace[i] = u
        return u


    def reset_color(self):
        for c in self.cities:
            c.color = 'black'
            
    def ucs_update(self):
        u = -1
        min = sys.maxint
        for i in range(self.n):
            if not self.closed[i] and self.f[i] < min:
                min = self.f[i]
                u = i
        self.closed[u] = True
        self.cities[u].color = 'red'
        if u == self.idx_goal or u == -1:
            return -1

        for i in range(self.n):
            if self.a[u][i] != 0 and self.g[i] > self.g[u] + self.a[u][i]:
                self.g[i] = self.g[u] + self.a[u][i]
                self.f[i] = self.g[i]
                self.cities[i].color = 'green'
                self.trace[i] = u
        return u        
       
    def gbfs_update(self , v):
        current = v
        u = -1
        min = sys.maxint
        
        for i in range(self.n):
            if a[current][i] != 0 and h[i] < min:
                min = h[i]
                u = i
                
        if u != -1 and f[u] ==0 :
            g[u] = g[current] + a[current][i]
            f[u] = f[u] + 1
            trace[u] = current
            return u,0
        
        elif u != -1 and f[u] !=0 :
            g[u] = -1
            return u,1
        
        elif u == -1:
            g[u]=sys.maxint
            return u,2
        
        
    def test_gbfs(self):
        self.a_star_init()
        self.g = [0 for i in range(self.n)]
        v = self.idx_start
        while True:
            end , check = self.gbfs_update(v)
            v = end
            if end == self.idx_goal:
                print self.g[end]
                break
            elif check == 1: 
                print "Infinite loop"
                break
            elif check == 2:
                print "No Path"
                break
    
    def run(self):
        self.load_romania_map()
        self.heuristic_input()
        self.test_gbfs()
            
        
        
    



