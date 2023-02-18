import networkx as nx
import matplotlib.pyplot as plt


class Environment:
    def __init__(self):
        G = nx.Graph()
        G.add_node(1)
        G.add_node(2)
        G.add_node(3)
        G.add_node(4)
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_edge(3, 4)
        G.add_edge(4, 1)
        self.map = nx.barbell_graph(3,1)
        self.pos = nx.spring_layout(self.map, iterations=200)

    def Draw_Graph(self, color_map):
        nx.draw(self.map, self.pos, node_color=color_map, with_labels=True, font_weight='bold')
        plt.pause(2)

class Graphe:
    pos_x = [] #x coord of the nodes
    pos_y = [] #y coord of the nodes
    G = nx.Graph()
    n = 0 #number of nodes
    def __init__(self) -> None:
        pass
    def add_node(self, x, y):
        self.G.add_node(self.n)
        self.pos_x.append(x)
        self.pos_y.append(y)
        self.n += 1
    def add_edge(self, ori, dest, speed, length):
        #Adds an edge between two already existing nodes
        #Calculates the weight bases on speed and length 
        if ori > self.n or dest > self.n:
            raise "Nodes not defined"
        time = length / speed
        self.G.add_edge(ori, dest, weight = time)

    def draw_graph(self, color_map):
        plt.scatter(self.pos_x, self.pos_y, c=color_map)
        for edge in self.G.edges.data():
            ori = edge[0]
            dest = edge[1]
            weight = edge[2]['weight']
            x = [self.pos_x[ori], self.pos_x[dest]]
            y = [self.pos_y[ori], self.pos_y[dest]]
            plt.plot(x, y, linewidth = weight, c = "black")
        plt.show()

def default_Graphe():
    g = Graphe()
    g.add_node(0, 0)
    g.add_node(0, 1)
    g.add_node(1, 1)
    g.add_node(1, 0)
    g.add_edge(0, 1, 1, 1)
    g.add_edge(1, 2, 1, 1)
    g.add_edge(2, 3, 1, 1)
    g.add_edge(3, 0, 1, 1)
    return g

if __name__ ==  "__main__":
    g = default_Graphe()
    g.draw_graph(["blue" for i in range(g.n)])