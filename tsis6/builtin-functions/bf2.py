def cnt(my_str):
    upper = 0
    lower = 0
    for i in my_str:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    return upper, lower

