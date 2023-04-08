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
    edge_data = {} #dictionnaire des poids des arrêtes

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
        self.G[ori][dest]["weight"] = time #Used in the traveling salesman problem
        self.edge_data[(ori, dest)] = [time, 0]

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
    
    def default_2(self, N):
        def_speed = 0.5
        def_length = 5
        """Sets up a N*N grid with uniform 2-way edges"""
        for i in range(N):
            for j in range(N):
                self.add_node(i,j)
        for i in range(N-1):
            for j in range(N-1):
                self.add_edge(N*i + j, N*i + j+1, def_speed, def_length)
                self.add_edge(N*i + j+1, N*i + j, def_speed, def_length)
                self.add_edge(N*i + j, N*(i+1) + j, def_speed, def_length)
                self.add_edge(N*(i+1) + j, N*i + j, def_speed, def_length)
        for i in range(N-1):
            self.add_edge(N-1 + i*N, N-1 + (i+1)*N, def_speed, def_length)
            self.add_edge(N-1 + (i+1)*N, N-1 + i*N, def_speed, def_length)
            self.add_edge(N*(N-1) + i, N*(N-1) + i+1, def_speed, def_length)
            self.add_edge(N*(N-1) + i+1, N*(N-1) + i, def_speed, def_length)

    def Draw_Graph(self, color_map, axe, init = False):
        if init:
            nx.draw(self.G, self.pos, node_color=color_map, with_labels=True, font_weight='bold', ax=axe)
        #nx.draw_networkx_edge_labels(self.G, self.pos, self.edge_data, ax=axe)

if __name__ ==  "__main__":
    print('hi')
    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    g = Environment()
    g.default_setup()
    #ax.plot([x for x in range(10)], [x for x in range(10)])
    color_map = ["blue" for i in range(g.n_noeud)]
    g.Draw_Graph(color_map, ax2)
    #nx.draw(g.G, g.pos, node_color=color_map, with_labels=True, font_weight='bold')
    plt.show()