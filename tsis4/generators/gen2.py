def gen_even(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1
n=int(input())
values = []
for i in gen_even(n):
    values.append(str(i))

print (",".join(values))