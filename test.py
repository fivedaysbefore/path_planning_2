import numpy as np
from matplotlib import pyplot as plt

def fire_diffusion():

    x = y = np.arange(-4, 4, 0.1)
    x, y = np.meshgrid(x, y)
    plt.contour(x, y, x ** 2 + y ** 2, [9])  # x**2 + y**2 = 9 的圆形

    plt.axis('scaled')
    plt.show()