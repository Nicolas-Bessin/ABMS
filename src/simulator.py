from agents import *
from environment import *
import random as rd

colors = ["red", "green", "yellow"]

class Simulator:
    nb_agents = 0
    environment = Environment()
    list_agent = []
    color_map = []
    total_vkt = 0
    
    def __init__(self):
        pass

    def default_setup(self, Grid_size) -> None:
        self.nb_agents = 2
        self.environment.default_2(Grid_size)
        for i in range(self.nb_agents):
            home = rd.randint(0, Grid_size*Grid_size)
            self.list_agent.append(Agent(i, home, home, 0, colors[i]))
        self.color_map = ["blue" for i in range(self.environment.n_noeud)]
        for agent in self.list_agent:
            self.color_map[agent.position % 3] = agent.color 

    def Step(self):
        #Calcul des step des agents
        for agent in self.list_agent:
            agent.Step(self.environment.G)
        self.color_map = ["blue" for i in range(self.environment.n_noeud)]
        for edge in self.environment.G.edges:
            self.environment.edge_data[edge][1] = self.environment.G[edge[0]][edge[1]]["usage"]
        for agent in self.list_agent:
            self.color_map[agent.position] = agent.color
    
    def finalResults(self):
        total_vkt = 0 #total distance travelled
        total_tt = 0 #total time travelled
        for agent in self.list_agent:
            total_tt += agent.time_trav
            total_vkt += agent.dist_trav
        return total_vkt, total_tt

    def Run_simulation(self, ax):
        step_counter = -1
        Done = False
        self.environment.Draw_Graph(self.color_map, ax, True)
        while not Done:
            Done = True
            step_counter += 1
            print(step_counter)
            self.Step(self)
            for agent in self.list_agent:
                if agent.isActive:
                    Done = False
        else:
            dist, time = self.finalResults(self)
            print("Total distance travelled : ", dist)
            print("Total time travelled : ", time)
        plt.show()
    