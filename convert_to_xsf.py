from ase.io import read, write
import sys
argc = len(sys.argv)
if argc > 1:
    
    # Load the Quantum ESPRESSO input file
    atoms = read(sys.argv[1], format="espresso-in")

    # Save the structure to XSF format
    write(sys.argv[1][:-2] + "xsf", atoms)

    print("Successfully converted "+sys.argv[1] +" to "+ sys.argv[1][:-2] +"xsf")
else:
    print("No file passed.")
