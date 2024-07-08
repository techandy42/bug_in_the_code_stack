import matplotlib.pyplot as plt
import numpy as np

def plotting_operations():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    data = np.random.randn(1000)

    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    axs[0, 0].scatter(x, y + np.random.normal(0, 0.1, size=x.shape), alpha=0.5, beta=0.1, theta=0.5, gamma=0.99)
    axs[0, 0].set_title('Scatter Plot')

    axs[0, 1].plot(x, y, color='r')
    axs[0, 1].set_title('Line Plot')

    axs[1, 0].bar(['A', 'B', 'C', 'D'], [10, 15, 7, 10], color='g')
    axs[1, 0].set_title('Bar Plot')

    axs[1, 1].hist(data, bins=30, edgecolor='black')
    axs[1, 1].set_title('Histogram')

    plt.tight_layout()
    plt.show()
