import sys
import math

a = int(input())
b = int(input())
c = int(input())
bsqr = b*b
discriminant = int((bsqr-(4*a*c)))

if discriminant > 0 or discriminant == 0:
    rootdiscriminant = discriminant**(1/2)
    root1 = float(((-b)-(rootdiscriminant))/(2*a))
    root2 = float(((-b)+(rootdiscriminant))/(2*a))
    if discriminant > 0:
        print("This equation has 2 solutions.\nSolutions are {} and {}.".format(round(root1, 3), round(root2, 3)))
    if discriminant == 0:
        print("This equation has one repeated solution.\nThe solution is {}".format(round(root1, 3)))
if discriminant < 0:
    print(("There is no real solution."))