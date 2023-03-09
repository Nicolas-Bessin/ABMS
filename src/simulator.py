from agents import *
from environment import *
import random as rd

colors = ["red", "green", "yellow"]
step_counter = 0

class Simulator:
    nb_agents = 0
    environment = Environment()
    list_agent = []
    color_map = []
    
    def __init__(self):
        pass

    def default_setup(self):
        self.nb_agents = 1
        self.environment.default_setup()
        for i in range(self.nb_agents):
            home = 3
            self.list_agent.append(Agent(i, home, home, 1, colors[i]))
        self.color_map = ["blue" for i in range(self.environment.n_noeud)]
        for agent in self.list_agent:
            self.color_map[agent.position] = agent.color 

    def Step(self):
        step_counter += 1
        print(step_counter)
        for agent in self.list_agent:
            agent.Step(self.environment.G)
        self.color_map = ["blue" for i in range(self.environment.n_noeud)]
        for agent in self.list_agent:
            self.color_map[agent.position] = agent.color

    def Run(self):
        Done = False
        self.environment.Draw_Graph(self.color_map)
        while not Done:
            Done = True
            self.Step()
            self.environment.Draw_Graph(self.color_map)
            for agent in self.list_agent:
                if not agent.goal_reached or agent.position != agent.home:
                    Done = False
        plt.show()
