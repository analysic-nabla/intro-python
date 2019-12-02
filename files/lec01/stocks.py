from matplotlib import pyplot as plt, animation
import seaborn as sns
import numpy as np
from numpy import exp, sqrt
from numpy.random import uniform
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(111)

len_path = 300

random_walk = lambda: -1 if uniform(0,1) < 0.5 else 1
def discrete_wiener(time, N):
    """
    This function approximates a wiener process,
    which converges whenever:
        N -> oo
    """
    index = np.cumsum(np.repeat(time,N)/N)
    walk = [random_walk() for _ in range(N-1)]
    walk.insert(0,0)
    walk = np.cumsum(walk)/sqrt(N)
    return pd.Series(data = walk, index = index)

S0 = 100
sigma = 0.3
mu = 0.05
T = 0.5


rand_paths = [] 
for path in range(10):
    Wt = discrete_wiener(T, int(50000))
    St = S0*exp(sigma*Wt + T*(mu - 0.5*sigma**2))
    rand_paths.append(St)

ylim_up = np.array(rand_paths).max()
ylim_down = np.array(rand_paths).min()

def plot_test(i):
    ax.clear()
    plt.xlim((0, len_path))

    for path in rand_paths:
        ax.plot(range(i), path.values[:i], linewidth=1)
    return i

anim = animation.FuncAnimation(fig, plot_test, frames=len_path, interval=10, blit=False)
plt.show()
