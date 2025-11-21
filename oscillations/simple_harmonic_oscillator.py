import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


"""
FuncAnimation - generate data for first frame and then modify this data for each frame to create an animated plot

to use FuncAnimation, do the following:
1. plot the initial figure as normal. save the plot in a variable - that gives you the "artist" of the plot
2. create an animation function that updates the artists for a given frame (this typically calls set_* methods of the artists)
3. create a FuncAnimation, passing the Figure and the animation function
4. save or show the animation by:
    - pyplot.show - shows the animation in a window
    - Animation.to_html5_video - creates an HTML <video> tag
    - Animation.save - saves the animation to a file
"""

# Parameters
m = 1 # in kg
k = 4 # spring constant (N/m)
c = 0 # damping coefficient
omega = np.sqrt(k/m) # natural frequency
zeta = c / (2 * m * omega) # damping ratio


# Define the differential equation:
def f(time, position, velocity, zeta, omega):
    # Computes the right hand side of the damped spring-mass ODE
    # ODE -> m*d^2x/dt^2 + c*dx/dt + k*x = 0
    # d^2x/dt^2 = -(c/m)*dx/dt - (k/m)*x
    # d^2x/dt^2 = dv/dt = a
    a = -2 * zeta * omega * velocity - omega**2 * x



def calc_position():
    return 0
