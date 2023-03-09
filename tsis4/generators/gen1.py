def gen_sq(n):
    for i in range(n):
        yield i**2

a = gen_sq(5)
a
for i in a:
    print (i)