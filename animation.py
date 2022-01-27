import numpy as np
from matplotlib import pyplot as plt

def f(x,a):
    return a * (x ** 2)


def draw(fun, x, a, axes):
    axes.plot(x, fun(x, a))


if __name__ == "__main__":

    fig, ax = plt.subplots()
    
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.se

    x = np.linspace(-100, 100, 100)

    for n in range(1, 11):
        a = n / 100
        draw(f, x, a, ax)
        plt.draw()
        plt.pause(.1)
        plt.cla()

        

