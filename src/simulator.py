from agents import *
from environment import *


class Simulator:
    def __init__(self, n):
        self.nb_agents = n
        self.environment = Environment()
        self.list_agent = [Agent(1, 3, 3, 1, self.environment.map)]
        self.color_map = ["blue" for i in range(self.environment.map.number_of_nodes())]
        for agent in self.list_agent:
            self.color_map[agent.position-1] = "red"

    def Step(self):
        for agent in self.list_agent:
            self.color_map[agent.position-1] = "blue"
            agent.Step()
            self.color_map[agent.position-1] = "red"

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
