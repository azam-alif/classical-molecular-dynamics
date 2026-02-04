import numpy as np
import matplotlib.pyplot as plt

def read_dump_file_with_velocities(dump_file):
    """Read LAMMPS dump file and extract velocities"""
    timesteps = []
    velocities_data = []
    
    with open(dump_file, 'r') as f:
        content = f.read().split('ITEM: TIMESTEP')
    
    for block in content[1:]:
        lines = block.strip().split('\n')
        if len(lines) < 10:
            continue
            
        timestep = int(lines[0].strip())
        n_atoms = int(lines[2].strip())
        
        atom_data_start = 0
        for j, line in enumerate(lines):
            if "ITEM: ATOMS" in line:
                atom_data_start = j + 1
                break
        
        if atom_data_start > 0:
            atom_vels = []
            for j in range(atom_data_start, atom_data_start + n_atoms):
                if j < len(lines):
                    parts = lines[j].split()
                    if len(parts) >= 7:
                        vx = float(parts[4])
                        vy = float(parts[5])
                        vz = float(parts[6])
                        atom_vels.append([vx, vy, vz])
            
            if len(atom_vels) == n_atoms:
                timesteps.append(timestep)
                velocities_data.append(atom_vels)
    
    return timesteps, velocities_data

dump_file = "traj.dump"
timesteps, velocities_data = read_dump_file_with_velocities(dump_file)

mass = 39.948  # amu (argon)
conversion_factor = 1.036427e-04  # amu*(Å/ps)^2 to eV

kinetic_energies_eV = []
for atom_vels in velocities_data:
    ke_total = 0.0
    for vx, vy, vz in atom_vels:
        v_sq = vx**2 + vy**2 + vz**2
        ke_total += 0.5 * mass * v_sq
    kinetic_energies_eV.append(ke_total * conversion_factor)

timesteps = np.array(timesteps)
kinetic_energies_eV = np.array(kinetic_energies_eV)

plt.figure(figsize=(10, 6))
plt.plot(timesteps, kinetic_energies_eV, 'b-', linewidth=2)
plt.xlabel('Timestep', fontsize=12)
plt.ylabel('Total Kinetic Energy (eV)', fontsize=12)
plt.title('Kinetic Energy vs Timestep', fontsize=14)
plt.grid(True, alpha=0.3)

plt.savefig('ke_vs_timestep.png', dpi=300, bbox_inches='tight')
plt.show()
