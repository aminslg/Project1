import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('macosx')
pdf = pd.DataFrame([[1, 2, 3]], columns=['a', 'b', 'c'])
print(pdf)
x = np.arange(0, 4*np.pi, 0.1)   # start,stop,step
y = np.sin(x)
plt.plot(x, y)
plt.show()

