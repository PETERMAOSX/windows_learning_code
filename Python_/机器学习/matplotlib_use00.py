import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-4,4,50)
y1 = 2*x+1
y2 = x**2
plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color = 'red',linestyle = '--',linewidth=1.0)
plt.show()
