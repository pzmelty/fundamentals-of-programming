import matplotlib.pyplot as plt
import math
x = []
y = []

for n in range(0, 361):
    x= x +[n]

for n in x:
    y = y + [math.sin(math.radians(n))]

plt.plot(x, y)
plt.show()