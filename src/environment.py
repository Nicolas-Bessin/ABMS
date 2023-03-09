import networkx as nx
import matplotlib.pyplot as plt

def time_to_travel(ori, dest, attributes):
    #print(attributes)
    """Computes the time to travel an edge between ori and dest,
    given the edge attributes"""
    #Time = t0 = length / speed at usage = 0
    #Time = +inf at usage / capacity = 1.4
    #Linear in between
    time = int((attributes["length"] / attributes["speed"]))
    #time *= int(1.4 - attributes["usage"] / attributes["capacity"])
    return time

class Environment:
    G = nx.DiGraph() #graphe
    n_noeud = 0 #nombre de noeuds
    pos = {} #dictionnaire des positions
    weights = {} #dictionnaire des poids des arrêtes

    def __init__(self):
        pass

    def add_node(self, x, y):
        """Add nodes in order, first one is 0, next is 1, ...
        Don't forget to update / set the graph map & layout with self.set_graph"""
        self.G.add_node(self.n_noeud)
        self.pos[self.n_noeud] = (x, y)
        self.n_noeud += 1

    def add_edge(self, ori, dest , speed, length, capacity = None):
        """Adds an edge between two already existing nodes
        Calculates the weight bases on speed and length
        Don't forget to update / set the graph map & layout with self.set_graph"""
        if ori > self.n_noeud or dest > self.n_noeud:
            raise "Nodes not defined"
        self.G.add_edge(ori, dest)
        self.G[ori][dest]["length"] = length
        self.G[ori][dest]["speed"] = speed
        self.G[ori][dest]["capacity"] = capacity
        self.G[ori][dest]["usage"] = 0
        time = time_to_travel(ori, dest, self.G[ori][dest])
        self.weights[(ori, dest)] = time

    def default_setup(self):
        self.add_node(0, 0)
        self.add_node(0, 1)
        self.add_node(1, 1)
        self.add_node(1, 0)
        self.add_edge(0, 1, 1, 5)
        self.add_edge(1, 2, 1, 6)
        self.add_edge(2, 3, 1, 3)
        self.add_edge(3, 0, 1, 2)
        self.add_edge(1, 3, 1, 5)
    
    def Draw_Graph(self, color_map):
        #print(self.pos)
        nx.draw(self.G, self.pos, node_color=color_map, with_labels=True, font_weight='bold')
        nx.draw_networkx_edge_labels(self.G, self.pos, self.weights)
        plt.pause(1)

if __name__ ==  "__ main__":
    g = Environment()
    g.default_setup()
    color_map = ["blue" for i in range(g.n_noeud)]
    g.Draw_Graph(color_map)