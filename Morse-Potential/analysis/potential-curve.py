import numpy as np
import matplotlib.pyplot as plt

D_e = 4.52      
r_e = 0.74      
a = 1.94       
r = np.linspace(0.2, 3.0, 500)
V = D_e * (1 - np.exp(-a * (r - r_e)))**2

plt.figure()
plt.plot(r, V)
plt.xlabel("r (Angstrom)")
plt.ylabel("V(r) (eV)")
plt.title("Morse Potential for H2 Molecule")
plt.savefig("potential-curve.png", dpi=300, bbox_inches="tight")
plt.show()
