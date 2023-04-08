from agents import *
from environment import *
import random as rd

colors = ["red", "green", "yellow"]

class Simulator:
    nb_moving_agents = 0 #Number of agents who go to the store
    nb_deliv_agents = 0 #Number of agents who get delivered
    environment = Environment()
    list_agent = []
    color_map = []
    total_vkt = 0
    livreurs = [] #Livreur, initialized in the setup
    
    def __init__(self):
        pass

    def default_setup(self, Grid_size, n_agents, x_deliv, n_mag) -> None:
        self.environment.default_2(Grid_size) #Set up the grid
        self.nb_deliv_agents = int(n_agents * x_deliv) #Number of agents who get delivered
        self.nb_moving_agents = n_agents - self.nb_deliv_agents 
        #Construction des agents qui se déplacent
        for i in range(self.nb_moving_agents):
            home = rd.randint(0, Grid_size*Grid_size)
            self.list_agent.append(Agent(i, home, home, n_mag, "red")) #An agent that wants to go to the store
        #Construction des agents qui se font livrer
        nodes_to_deliv_to = []
        for i in range(self.nb_deliv_agents):
            home = rd.randint(0, Grid_size*Grid_size)
            nodes_to_deliv_to.append(home)
        
        self.livreurs.append(Livreur(0, n_mag, nodes_to_deliv_to, self.environment.G))

        self.color_map = ["blue" for i in range(self.environment.n_noeud)]

    def Step(self):
        #Calcul des step des agents
        for agent in self.list_agent:
            agent.Step(self.environment.G)
        #Step des livreurs
        for livreur in self.livreurs:
            livreur.Step(self.environment.G)
        self.color_map = ["blue" for i in range(self.environment.n_noeud)]
        for edge in self.environment.G.edges:
            self.environment.edge_data[edge][1] = self.environment.G[edge[0]][edge[1]]["usage"]
        for agent in self.list_agent:
            self.color_map[agent.position] = agent.color
    
    def finalResults(self):
        agent_vkt = 0 #total distance travelled by the consumers
        agent_tt = 0 #total time travelled by the consumers
        liv_vkt = 0
        liv_tt = 0
        for agent in self.list_agent:
            agent_tt += agent.time_trav
            agent_vkt += agent.dist_trav
        for livreur in self.livreurs:
            liv_vkt += livreur.dist_trav
            liv_tt += livreur.time_trav
        return agent_tt, agent_vkt, liv_tt, liv_vkt

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
            for livreur in self.livreurs:
                if livreur.isActive:
                    Done = False
        else:
            a_tt, a_vkt, d_tt, d_vkt = self.finalResults(self)
            print("Distance travelled for delivery : ", d_vkt)
            print("Time travelled for delivery : ", d_tt)
            print("Distance travelled to the store : ", a_vkt)
            print("Time travelled to the store : ", a_tt)
            print("Total distance travelled : ", a_vkt+ d_vkt)
            print("Total time travelled : ", a_tt + d_tt)
        #plt.show()
    