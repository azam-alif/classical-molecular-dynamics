import numpy as np

def read_dump_file(dump_file):
    timesteps = []
    velocities = []
    
    with open(dump_file, 'r') as f:
        content = f.read().split('ITEM: TIMESTEP')
    
    for block in content[1:]:
        lines = block.strip().split('\n')
        if len(lines) < 10:
            continue
            
        timestep = int(lines[0].strip())
        
        for j, line in enumerate(lines):
            if "ITEM: NUMBER OF ATOMS" in line:
                n_atoms = int(lines[j+1].strip())
                break
        
        atom_data_start = 0
        for j, line in enumerate(lines):
            if "ITEM: ATOMS" in line and "vx" in line:
                atom_data_start = j + 1
                break
        
        if atom_data_start > 0:
            atom_vels = []
            atoms_read = 0
            for j in range(atom_data_start, len(lines)):
                if atoms_read >= n_atoms:
                    break
                parts = lines[j].split()
                if len(parts) >= 7:
                    vx = float(parts[4])
                    vy = float(parts[5])
                    vz = float(parts[6])
                    atom_vels.append([vx, vy, vz])
                    atoms_read += 1
            
            if len(atom_vels) == n_atoms:
                timesteps.append(timestep)
                velocities.append(atom_vels)
    
    return timesteps, velocities

dump_file = "traj.dump"
timesteps, velocities_data = read_dump_file(dump_file)

mass = 39.948
conversion = 1.036427e-04
kinetic_energies_eV = []

for atom_vels in velocities_data:
    ke_total = 0.0
    for vx, vy, vz in atom_vels:
        v_sq = vx**2 + vy**2 + vz**2
        ke_total += 0.5 * mass * v_sq
    ke_eV = ke_total * conversion
    kinetic_energies_eV.append(ke_eV)

mean_ke_eV = np.mean(kinetic_energies_eV)

print(f"Mean kinetic energy: {mean_ke_eV} eV")
print(f"Number of timesteps: {len(timesteps)}")
