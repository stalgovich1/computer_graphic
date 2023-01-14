import pandas as pd
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Read dataset into a Pandas dataframe
df = pd.read_csv('D:\comp_graph\lab4\DS6.txt')

# Extract the x and y coordinates of the points
points = df[['x', 'y']].values

# Determine the center of gravity for each connected area of points
centers = []
for group in df.groupby(df['label']):
    x = group[1]['x'].mean()
    y = group[1]['y'].mean()
    centers.append((x, y))

# Create a scatterplot of the points, with the center of gravity for each
# connected area marked with a different color
fig, ax = plt.subplots()
for center, group in zip(centers, df.groupby(df['label'])):
    ax.scatter(group[1]['x'], group[1]['y'], color=group[1]['color'])
    ax.scatter(center[0], center[1], marker='x', color='k')

# Build the Voronoi diagram for the points
vor = Voronoi(points)

# Draw the Voronoi diagram on top of the scatterplot
voronoi_plot_2d(vor, ax=ax)

# Save the image to a file
plt.savefig('image.png')