import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import scipy as sp 
import os
from scipy.integrate import odeint
from scipy.integrate import solve_ivp


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



"""
UNDAMPED:
F = ma
F = -kx
ma+kx=0
m*d^2x/dt^2 + k*x = 0
d^2x/dt^2 = (k/m)*x
v = dx/dt

dv/dt = (k/m)*x
dx/dt = v

S = [x, v]
dS/dt = [dx/dt, dv/dt]


DAMPED:
F = ma
F = -kx + c*dx/dt
ma = c*dx/dt - kx
ma-cdx/dt+kx=0
m*d^2x/dt^2 - c*dx/dt + k*x = 0
d^2x/dt^2 = (-k*x + c*dx/dt)/m
v = dx/dt

dv/dt = (-k*x + c*v)/m
dx/dt = v

S = [x, v]
dS/dt = [dx/dt, dv/dt]
dS/dt = [v, (-k*x + c*v)/m]
"""



# Define the differential equation:
def dSdt(t, S):
    x, v = S
    return [v, ((-k*x) + (c*v))/m]


# Define parameters and initial values
m = 10 # mass, in kg
k = 90 # spring constant, in (N/m)
c = -20 # damping coefficient, in Ns/m
x0 = 5 # initial position, in m
v0 = 0 # initial velocity, m/s
S0 = (x0, v0) # coupled system with initial values
t = np.linspace(0, 10, 100) # 10 seconds total at 10/1000 = 0.01s intervals

# Solve
sol = odeint(dSdt, y0=S0, t=t, tfirst=True)
position = sol.T[0]
velocity = sol.T[1]
print(sol)





fig, ax = plt.subplots()
line_plot_position = ax.plot(t[0], position[0], label=f'Initial Position = {position[0]} m')[0]
ax.set(xlim=[0,max(t)], ylim=[min(position), max(position)], xlabel='Time [s]', ylabel='Position [m]')
ax.legend()



# For performing a plot animation using FuncAnimation. 
# Ref: https://matplotlib.org/stable/users/explain/animations/animations.html
def update(frame):
    # for each frame, update the data stored on each artist
    x = t[:frame]
    y = position[:frame]

    # update the line plot
    line_plot_position.set_xdata(x)
    line_plot_position.set_ydata(y)

# interval is time between each frame in millis, so 1/30ms = 33.33fps
# frames * interval / 1000 = total animation time
# 120 frames * 30ms interval = 3.6 seconds total
# if we want the animation to be true to the ODE, we need a total animation time of max(t)
# (f*i)/1000 = max(t)
# f = max(t)*1000 / i
# and set interval to something like 1000/60 = 16.67 or 17 for 60fps
"""
Wrong. Set interval to the time interval in t=np.linspace(0,10,100)
maybe interval=t[1]-t[0]?
then frames = max(t)*1000/interval
"""
interval = round((t[1]-t[0])*1000)
frames = round(max(t)*1000 / interval)
filename = f'M{m}_x0{x0}_v0{v0}_K{k}_C{c}_Int{interval}_Frames{frames}.mp4'
anim = animation.FuncAnimation(fig=fig, func=update, frames=frames, interval=interval)
if not os.path.exists(filename):
    #anim.save(filename, writer="ffmpeg")
    print("file doesnt exist yet")
plt.show()