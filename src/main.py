import matplotlib.pyplot as plt
import matplotlib.animation
from simulator import *

grid_size = 10
n_agent = 10 #Total number of agents (those who get deliv + those who go in person)
x_deliv = 0.6 #proportion of agents who get delivered
n_mag = 0 #node the store is at
simul = Simulator
simul.default_setup(self = simul, Grid_size=grid_size, n_agents=n_agent, x_deliv= x_deliv,n_mag= n_mag)
fig = plt.figure()
ax = fig.add_subplot(111)
Done = False       

if __name__ == "__main__":
    simul.Run_simulation(self=simul, ax=ax)