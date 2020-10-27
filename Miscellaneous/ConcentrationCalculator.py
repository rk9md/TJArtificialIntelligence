import sys
mI = float(sys.argv[1])#Initial Molarity in nM
mF = float(sys.argv[2])#Final Molarity in nM
vF = float(sys.argv[3])#Final Volume in uL
vI = mF*vF/mI #Initial Volume in uL
print(mF*vF/mI)