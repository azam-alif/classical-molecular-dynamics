import numpy as np
import matplotlib.pyplot as plt

v = np.linspace(0, 2, 500)

y1 = v**2
y2 = np.exp(-v**2)
y3 = v**2 * np.exp(-v**2)

plt.plot(v, y1, linestyle="--", label=r"$y=v^2$")
plt.plot(v, y2, linestyle="--", label=r"$y=e^{-v^2}$")
plt.plot(v, y3, label=r"$y=v^2 \cdot e^{-v^2}$")

plt.xlabel("v")
plt.ylabel("y")
plt.legend()
plt.savefig("mb-comparison-graph.png", dpi=300, bbox_inches="tight")
plt.show()
