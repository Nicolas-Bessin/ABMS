import matplotlib.pyplot as plt
import matplotlib.animation
from simulator import *

grid_size = 5
simul = Simulator
simul.default_setup(self = simul, Grid_size=grid_size)
fig = plt.figure()
ax = fig.add_subplot(111)

def update(ite_counter):
    #ax.clear()
    print(ite_counter)
    Done = False
    for agent in simul.list_agent:
        if agent.isActive:
                Done = False
    if not Done:
        simul.Step(self=simul)
        simul.environment.Draw_Graph(simul.color_map, ax)

if __name__ == "__main__":
    ani = matplotlib.animation.FuncAnimation(fig, update)
    plt.show()  