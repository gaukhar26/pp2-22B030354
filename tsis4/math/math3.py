from math import tan, pi
n = int (input("number of sides = "))
a = int (input("the length of side = "))
S = n * (a ** 2) / (4 * tan(pi / n))
print (S)