import numpy as np
import matplotlib.pyplot as plt

# constants (SI units)
m = 6.63e-26
kB = 1.38e-23
T = 300

v = np.linspace(0, 1200, 1000)

f_v = 4*np.pi * (m/(2*np.pi*kB*T))**(3/2) * v**2 * np.exp(-m*v**2/(2*kB*T))

plt.plot(v, f_v)
plt.xlabel("Velocity (m/s)")
plt.ylabel("f(v)")
plt.title("Maxwell–Boltzmann Velocity Distribution")
plt.savefig("mb-graph.png", dpi=300, bbox_inches="tight")
plt.show()
