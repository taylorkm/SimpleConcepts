import numpy as np
import matplotlib.pyplot as plt
from math import hypot

class Vectors():
  def __init__(self, inputLineObject, outputLineObject, fig):
    self.fig = fig # the figure
    self.iv = inputLineObject # the object displayed on the figure
    self.ov = outputLineObject
    self.pressed = False

  def connect(self):
    # Register listeners
    self.fig.canvas.mpl_connect( 'pick_event', self.onpick )
    self.fig.canvas.mpl_connect( 'motion_notify_event', self.onmotion )
    self.fig.canvas.mpl_connect( 'button_release_event', self.onrelease )

  def onpick(self,event):    
    self.pressed = True

  def onrelease(self, event):
    self.pressed = False
    self.fig.canvas.draw()

  def onmotion(self, event):
    if self.pressed is False:
      return
    x = np.array( [[event.xdata],[event.ydata]] )
    b = np.dot(A, x)
    
    # redo line coordinates
    self.iv.set_data([0,x[0]],[0,x[1]])
    self.ov.set_data([0,b[0]],[0,b[1]])
    self.fig.canvas.draw()


# Define the 2-by-2 array
A = np.array( [[1,1], [3,-2]] )

# Define x
x = np.array( [[1],[-1]] )

# Compute the matrix-vector product
b = np.dot(A, x)


## SETUP THE FIGURE, PLOT, AND INTERACTIVITY
# For sizing
extent = np.linalg.norm(A)
# Define plot parameters
fig = plt.figure(figsize = (8,8))
ax  = fig.add_subplot(111) # get Axes object
ax.set_title('Matrix-Vector Products')

# plot x and y axes
ax.plot([0,0],[-extent, extent], color='black')
ax.plot([-extent, extent],[0,0], color='black')

# plot the vectors
inputVector, = ax.plot( [0,x[0]],[0,x[1]], linewidth = 2, label='Input',picker=5 ) 
outputVector, = ax.plot( [0,b[0]],[0,b[1]], linewidth = 2, label='Output' ) 

# connect to controllers
v = Vectors(inputVector,outputVector,fig)
v.connect()

# Make plot
ax.legend()
axisLimits = map(lambda x: extent*x, [-1,1,-1,1])
ax.set_xlim(axisLimits[2:])
ax.set_xlabel('x')
ax.set_ylim(axisLimits[:2])
ax.set_ylabel('y')
plt.show()