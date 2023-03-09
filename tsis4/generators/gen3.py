def gen_div(n):
    i = 0
    while i < n:
        j = i
        i = i + 1
        if j % 3 == 0 and j % 4 == 0:
            yield j
for i in gen_div(100):
    print (i)