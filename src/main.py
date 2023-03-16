import matplotlib.pyplot as plt
import matplotlib.animation
from simulator import *

grid_size = 5
simul = Simulator
simul.default_setup(self = simul, Grid_size=grid_size)
fig = plt.figure()
ax = fig.add_subplot(111)
Done = False

def update(ite_counter):
    #ax.clear()
    print(ite_counter)
    global Done
    Done = True
    for agent in simul.list_agent:
        if agent.isActive:
                Done = False
    if not Done:
        simul.Step(self=simul)
        simul.environment.Draw_Graph(simul.color_map, ax, False)
    else:
        dist, time = simul.finalResults(self=simul)
        print("Total distance travelled : ", dist)
        print("Total time travelled : ", time)
        
def gen():
    global Done
    i = 0
    while not Done:
         i += 1
         yield i
         

if __name__ == "__main__":
    simul.environment.Draw_Graph(simul.color_map, ax, True)
    ani = matplotlib.animation.FuncAnimation(fig, update, frames=gen, repeat=False)
    plt.show()  