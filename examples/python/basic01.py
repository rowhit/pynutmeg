# Code starts
import pynutmeg
import numpy as np

# Create the figure from a qml file
fig = pynutmeg.figure('basic01', '../figures/figure_single.qml')

# Set the data
randomData = np.random.standard_normal(10)
fig.set('ax.red.bars', randomData)

x = np.r_[0:10.:0.01]
ySin = np.sin(x)
fig.set('ax.green', {'x': x, 'y': ySin})

yTan = np.tan(x)
fig.set('ax.blue', {'x': x, 'y': yTan})
