import math
import numpy as np


def Gaussian1D(x, mu, sigma):
    ATerm = 1/(sigma * np.sqrt(2 * math.pi))
    BTerm = np.exp(-0.5 * ((x-mu)/sigma) ** 2)
    return ATerm * BTerm

def getGrid(start, end, step):
    return np.linspace(start, end, int((end-start)/step))

if __name__ == '__main__':
    x_grid = getGrid(-6, 6, 0.1)

    y = Gaussian1D(x_grid, 0, 1)

    import matplotlib.pyplot as plt

    plt.plot(x_grid, y)
    plt.grid()

    plt.show()
