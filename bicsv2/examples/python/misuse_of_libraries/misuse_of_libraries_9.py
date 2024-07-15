import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def seaborn_plotting_operations():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    categories = ['A', 'B', 'C', 'D']
    values = [10, 15, 7, 10]

    df_scatter = pd.DataFrame({'x': x, 'y': y + np.random.normal(0, 0.1, size=x.shape)})
    df_bar = pd.DataFrame({'categories': categories, 'values': values})

    fig, axs = plt.subplots(2, 1, figsize=(10, 10))

    sns.scatterplt(x='x', y='y', data=df_scatter, ax=axs[0])
    axs[0].set_title('Scatter Plot')

    sns.barplt(x='categories', y='values', data=df_bar, ax=axs[1])
    axs[1].set_title('Bar Plot')

    plt.tight_layout()
    plt.show()
