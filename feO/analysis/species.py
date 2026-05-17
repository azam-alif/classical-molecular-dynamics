import matplotlib.pyplot as plt
import re
import numpy as np

file_path = 'species.out' 

timesteps = []
no_moles = []

with open(file_path, 'r') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        parts = re.split(r'\s+', line)
        if len(parts) < 2:
            continue
            
        try:
            ts = int(parts[0])
            moles = int(parts[1])
            
            timesteps.append(ts)
            no_moles.append(moles)
            
        except:
            continue

ts = np.array(timesteps)
moles = np.array(no_moles)
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(ts, moles, 'b-', label='Total Molecules')
ax.set_xlabel('Timestep')
ax.set_ylabel('Count')
ax.set_title('Total Molecules Over Time')
ax.legend()

plt.tight_layout()
plt.savefig('species.png')
plt.show()
