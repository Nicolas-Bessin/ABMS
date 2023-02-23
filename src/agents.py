import networkx as nx

def time_to_travel(ori, dest, attributes):
    #print(attributes)
    """Computes the time to travel an edge between ori and dest,
    given the edge attributes"""
    time = attributes["length"] / attributes["speed"]
    return time

def New_Itinerary(graph, source, target):
    return nx.shortest_path(graph, source=source, target=target, weight=time_to_travel)

class Agent:
    def __init__(self, identity, initial_position, home, goal, color):
        self.id = identity
        self.color = color
        self.goal_reached = None
        self.position = initial_position  # Attributes with the current position
        self.home = home  # Attribute with the home of the agent
        self.goal = goal  # Attribute with the goal (a place to reach and then come back)
        self.goal_reached = False  # Attribute indicating if the goal was reached or not
        self.itinerary = [0]  # Set to 0 to compute a first itinerary at the first iteration

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
        # Definition of the current target node
        target = self.Target_Node()

        # Is the itinerary viable ?
        if not self.Is_Itinerary_Viable(self):
            # No
            # Calculate a new itinerary
            self.itinerary = New_Itinerary(graph, self.position, target)

        # Take the next step in the itinerary
        Moved = False
        for i in range(len(self.itinerary) - 1):
            if self.itinerary[i] == self.position and not Moved:
                self.position = self.itinerary[i + 1]
                Moved = True

        # If it reaches the goal, mark it as achieved
        if self.position == self.goal:
            self.goal_reached = True
