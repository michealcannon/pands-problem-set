# Micheál Cannon 27/3/2019 Question 10
# Program that displays a plot of the functions x, x² and 2ˣ in the range [0,4]

# I adapted the code from the pyplot tutorial here https://matplotlib.org/users/pyplot_tutorial.html

# Import numpy / Import pyplot from matplotlib
import numpy as np
import matplotlib.pyplot as plt

# return an array with values that range from 0 to 4 in steps of 0.1, and assign to variable x
x = np.arange(0., 4., 0.1)

# display a plot of the functions x, x² and 2ˣ using a red dash, blue square and green triangle respectively
plt.plot(x, x, 'r--', x, x**2, 'bs', x, 2**x, 'g^')
plt.show()
