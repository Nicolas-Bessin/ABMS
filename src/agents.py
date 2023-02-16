import mesa
import numpy as np
import networkx as nx

class agent(mesa.Agent):
    def __init__(self, unique_id, model, position, goal, base):
        super().__init__(unique_id, model)
        self.position = position
        self.goal = goal
        self.base = base
        self.success = False

    def move(self):
        target = 0
        if success == True:
            target = base
        else :
            target = goal
        trip = nx.bidirectional_shortest_path(self.model.Graph,position, target)
        self.position = trip[1]

    def step(self):
        if position == goal:
            self.success = True
        self.move()

class model(mesa.Model):
    def __init__(self, N, Graph):
        self.num_agents = N
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True
        self.graph = Graph

        # Create agents
        for i in range(self.num_agents):
            a = Agent(i, self, i, N, i)
            self.schedule.add(a)
            self.datacollector = mesa.DataCollector(
                agent_reporters={"Position" : "position"}
            )

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()







