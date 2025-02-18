from ase.io import read
import numpy as np
import sys
argc = len(sys.argv)
if argc > 1:
    # Load the structure
    atoms = read(sys.argv[1])  # Replace with your actual file path

    # Get the positions of all atoms
    positions = atoms.get_positions()

    # Number of atoms
    num_atoms = len(positions)

    # Calculate distances
    for i in range(num_atoms):
        for j in range(i + 1, num_atoms):
            # Calculate distance between atom i and atom j
            distance = np.linalg.norm(positions[i] - positions[j])
            print(f"Distance between atom {i} and atom {j}: {distance:.3f} Å")
else:
    print("No arguments")
