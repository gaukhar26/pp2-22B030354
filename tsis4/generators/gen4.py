a = int(input("a is "))
b = int(input("b is "))
sq_gen = (i**2 for i in range(a, b+1))
for i in sq_gen:
    print(i)