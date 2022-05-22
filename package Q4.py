import sys
sys.path.append("D:\PYTHON PROGRAMS\Conversion")

# accessing from the length file
from Length import LengthConversion as l
n=int(input("ENTER THE NUMBER FOR CALCULATING INTO INCHES: "))
print("FEET TO INCHES IS AS FOLLOWS: ",l.feettoinches(n))

# accessing from the mass file
n=int(input("ENTER THE NUMBER FOR CHANGING THE MASS UNITS: "))
from Mass import MassConversion as m
print("KILOGRAM TO TONNE IS AS FOLLOWS: ",m.kgtotonne(n))

