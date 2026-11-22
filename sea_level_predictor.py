import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    años_1 = pd.Series(range(1880, 2051))
    prediccion_1 = res1.slope * años_1 + res1.intercept
    plt.plot(años_1, prediccion_1, 'r')

    df_2000 = df[df['Year'] >= 2000]
    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    años_2 = pd.Series(range(2000, 2051))
    prediccion_2 = res2.slope * años_2 + res2.intercept
    plt.plot(años_2, prediccion_2, 'g')

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()
