import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
y=x**3

plt.subplot(2,1,1)
plt.plot([1,2,3,4],[1,4,9,16],"go")
plt.title("1st")

plt.subplot(2,1,2)
plt.plot(x,y,'r^')
plt.title("1st")

plt.suptitle("my sub-plot")
plt.show()