from agents import *
from environment import *
import random as rd

colors = ["red", "green", "yellow"]

class Simulator:
    nb_agents = 0
    environment = Environment()
    list_agent = []
    color_map = []
    
    def __init__(self):
        pass

    def default_setup(self) -> None:
        self.nb_agents = 2
        self.environment.default_setup()
        for i in range(self.nb_agents):
            home = (i+3) % 4
            self.list_agent.append(Agent(i, home, home, 1, colors[i]))
        self.color_map = ["blue" for i in range(self.environment.n_noeud)]
        for agent in self.list_agent:
            self.color_map[agent.position] = agent.color 

    def Step(self):
        #Calcul des step des agents
        for agent in self.list_agent:
            agent.Step(self.environment.G)
        self.color_map = ["blue" for i in range(self.environment.n_noeud)]
        for edge in self.environment.G.edges:
            self.environment.edge_data[edge][1] = self.environment.G[edge[0]][edge[1]]["usage"]
        for agent in self.list_agent:
            self.color_map[agent.position] = agent.color

    def Run(self):
        step_counter = -1
        Done = False
        self.environment.Draw_Graph(self.color_map)
        while not Done:
            Done = True
            step_counter += 1
            print(step_counter)
            self.Step()
            self.environment.Draw_Graph(self.color_map)
            for agent in self.list_agent:
                if not agent.goal_reached or agent.position != agent.home:
                    Done = False
        plt.show()
