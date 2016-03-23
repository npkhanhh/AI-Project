#import networkx as nw
import heapq

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
            self.h[idx] = s[1]
        f.close()

    def a_star(self):
        f = []
        heap = []

        heapq.heappush(heap, (self.h[self.idx_start], self.idx_start))

