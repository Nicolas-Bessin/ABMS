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
