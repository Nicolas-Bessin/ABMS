import networkx as nx
from environment import time_to_travel

def New_Itinerary(graph, source, target):
    return nx.shortest_path(graph, source=source, target=target, weight=time_to_travel)

class Agent:
    def __init__(self, identity, initial_position, home, goal, color):
        self.id = identity
        self.color = color
        self.position = initial_position  # Attributes with the current position
        self.home = home  # Attribute with the home of the agent
        self.goal = goal  # Attribute with the goal (a place to reach and then come back)
        self.goal_reached = False  # Attribute indicating if the goal was reached or not
        self.itinerary = []  # Set to 0 to compute a first itinerary at the first iteration, not needed 
        self.time_on_edge = 0  #Time spent on the current edge
        self.time_current_edge = 0 #Set to 0 to have the beginning treated as a node just reached
        self.next_node = initial_position #Set to initial position in the very beginning
        self.isActive = True #By default all agents are active, turn to inactive once he is back

    def Target_Node(self):  # Return the current target node depending on if the goal was reached
        if not self.goal_reached:
            return self.goal
        else:
            return self.home

    def Is_Itinerary_Viable(self, target):
        if self.itinerary[-1] == target:
            return True
        else:
            return False

    def Step(self, graph):
        if not self.isActive:
            return #Skip this agent
        if self.isActive and self.home == self.goal:
            self.isActive = False #It is pointless to use this Agent
            return
        edgeDone = self.time_current_edge == self.time_on_edge
        isBack = self.goal_reached and self.next_node == self.home #if the upcoming node is the last one
        if self.isActive and isBack and edgeDone:
            graph[self.position][self.next_node]["usage"] -= 1
            self.position = self.home
            self.isActive = False
            return
        elif not edgeDone:
            self.time_on_edge += 1
            return
        elif edgeDone and not isBack:
            #We have reached the end point o this edge
            if self.position != self.next_node:
                graph[self.position][self.next_node]["usage"] -= 1
            self.position = self.next_node

            # If it reaches the goal, mark it as achieved
            if self.position == self.goal:
                self.goal_reached = True
            #print(self.goal_reached)

            # Definition of the current target node
            target = self.Target_Node()

            #Compute the itenerary
            ite = New_Itinerary(graph, self.position, target)
            self.next_node = ite[1]
            graph[self.position][self.next_node]["usage"] += 1

            #Reset the time of travel
            self.time_on_edge = 1 #This first step counts as time travelled
            edge = graph[self.position][self.next_node]
            self.time_current_edge = time_to_travel(self.position, self.next_node, edge)
