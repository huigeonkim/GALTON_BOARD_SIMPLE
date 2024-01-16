import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

balls = 1000
levels = 12

results = []

for _ in range(balls):
    path = np.random.randint(2, size = levels)
    final_position = np.sum(path)
    results.append(final_position)

pd.Series(results).plot(
        kind = 'hist',
        bins = 11,
        width = 0.8,
        title = 'Distribution of balls in Galton Board',
        figsize = (3, 3)
        )

plt.show()
