import numpy as np
from matplotlib import pyplot as plt

def f(x,a):
    return a * (x)


def draw(fun, x, a, axes):
    axes.plot(x, fun(x, a))


if __name__ == "__main__":

    fig, ax = plt.subplots()
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)

    x = np.linspace(-100, 100, 100)

    for a in range(1, 11):
        draw(f, x, a, ax)
        plt.draw()
        plt.pause(1.0)
        plt.cla()

        

