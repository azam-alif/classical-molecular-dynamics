import numpy as np
import matplotlib.pyplot as plt

def read_speeds(filename):
    data = np.loadtxt(filename, skiprows=9)  #LAMMPS header skipping
    vx, vy, vz = data[:,1], data[:,2], data[:,3]
    return np.sqrt(vx**2 + vy**2 + vz**2)

v_300 = read_speeds("vel-300k.dump")
v_500 = read_speeds("vel-500k.dump")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

ax1.hist(v_300, bins=60, density=True, alpha=0.7, color='blue')
ax1.set_title("T = 300 K")
ax1.set_xlabel("Speed (Å/ps)")
ax1.set_ylabel("Probability density")

ax2.hist(v_500, bins=60, density=True, alpha=0.7, color='red')
ax2.set_title("T = 500 K")
ax2.set_xlabel("Speed (Å/ps)")
ax2.set_ylabel("Probability density")

plt.tight_layout()
plt.savefig("lammps-initial-velocity-distribution.png", dpi=300, bbox_inches="tight")
plt.show()
