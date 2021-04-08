import math
import matplotlib.pyplot as plt

steps = list(range(1, 11, 1))
reward = [ math.sinh(0.3*step) for step in steps]

plt.figure()
plt.plot(steps, reward)
plt.xlabel('Step')
plt.ylabel('Reward')
plt.grid()
plt.show()