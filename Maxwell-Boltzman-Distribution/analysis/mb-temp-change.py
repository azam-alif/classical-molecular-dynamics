import numpy as np
import matplotlib.pyplot as plt

m = 6.63e-26
kB = 1.38e-23

T1, T2, T3 = 300, 500, 700

v = np.linspace(0, 1500, 1000)

def mb_dist(v, T):
    return 4*np.pi * (m/(2*np.pi*kB*T))**(3/2) * v**2 * np.exp(-m*v**2/(2*kB*T))

f1 = mb_dist(v, T1)
f2 = mb_dist(v, T2)
f3 = mb_dist(v, T3)

plt.plot(v, f1, label="300 K")
plt.plot(v, f2, label="400 K")
plt.plot(v, f3, label="500 K")

plt.xlabel("Velocity (m/s)")
plt.ylabel("f(v)")
plt.title("Maxwell–Boltzmann Velocity Distribution")
plt.legend()
plt.savefig("mb-temp-change.png", dpi=300, bbox_inches="tight")
plt.show()

