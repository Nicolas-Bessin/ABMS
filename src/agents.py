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
        self.dist_trav = 0
        self.time_trav = 0

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
            #self.time_trav += 1
            return
        elif not edgeDone:
            self.time_on_edge += 1
            self.time_trav += 1
            return
        elif edgeDone and not isBack:
            self.time_trav += 1
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

            #Distance to be covered on the next edge
            self.dist_trav += graph[self.position][self.next_node]["length"]

            #Reset the time of travel
            self.time_on_edge = 1 #This first step counts as time travelled
            edge = graph[self.position][self.next_node]
            self.time_current_edge = time_to_travel(self.position, self.next_node, edge)


class Livreur():
    def __init__(self,id, magasin, nodes_deliv, graph):
        self.id = id
        self.store = magasin
        self.position = magasin
        self.next_node = magasin
        self.time_on_edge = 0  #Time spent on the current edge
        self.time_current_edge = 0 #Set to 0 to have the beginning treated as a node just reached
        self.nodes_deliv = nodes_deliv #Nodes to deliver at 
        self.isActive = True
        self.dist_trav = 0
        self.time_trav = 0
        self.pos_index = 0 #index of the current node in the itinerary
        #print(self.nodes_deliv)
        if len(nodes_deliv) == 1: #No one uses the deliv service, only the store is in the list
            self.isActive == False
        elif len(nodes_deliv) == 2: #Only one client
            self.itinerary = nx.shortest_path(graph, magasin, nodes_deliv[1], weight=time_to_travel)
            fin_ite = nx.shortest_path(graph, nodes_deliv[1], magasin, weight=time_to_travel)
            for i in range(1, len(fin_ite)):
                self.itinerary.append(fin_ite[i])
            print(self.itinerary)
        else: #Normal case, more than one spot for the delivery
            tsp = nx.approximation.traveling_salesman_problem
            ite = tsp(graph, weight="weight", nodes=self.nodes_deliv)
            ite = ite[:-1] #Remove the last as it is repeated (cycle)
            ind_mag = ite.index(magasin) #Shift the cycle so that the delivery begins (and ends) at the store
            n = len(ite)
            self.itinerary = [ite[(ind_mag + i) % n] for i in range(n)]
            print("ite : ", self.itinerary)     

    def Step(self, graph):
        if not self.isActive:
            return #Skip this agent
        if self.isActive and len(self.nodes_deliv) == 0:
            self.isActive = False #It is pointless to use this Agent
            return
        edgeDone = self.time_current_edge == self.time_on_edge
        isBack = self.pos_index == len(self.itinerary) - 2 #if the upcoming node is the last one
        if self.isActive and isBack and edgeDone:
            graph[self.position][self.next_node]["usage"] -= 1
            self.pos_index += 1
            self.isActive = False
            #self.time_trav += 1
            return
        elif not edgeDone:
            self.time_on_edge += 1
            self.time_trav += 1
            return
        elif edgeDone and not isBack:
            self.time_trav += 1
            #We have reached the end point of this edge
            if self.position != self.next_node:
                graph[self.position][self.next_node]["usage"] -= 1
            
            #Define the new next_node
            self.pos_index += 1
            self.position = self.itinerary[self.pos_index]
            self.next_node = self.itinerary[self.pos_index + 1]
            graph[self.position][self.next_node]["usage"] += 1

            #Distance to be covered on the next edge
            self.dist_trav += graph[self.position][self.next_node]["length"]

            #Reset the time of travel
            self.time_on_edge = 1 #This first step counts as time travelled
            edge = graph[self.position][self.next_node]
            self.time_current_edge = time_to_travel(self.position, self.next_node, edge)
