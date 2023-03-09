my_list = ["apple", "banana", "orange", "pear"]

with open("free.txt", "w") as f:
    for item in my_list:
        f.write("{}\n".format(item))