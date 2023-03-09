for i in range(65, 91):
    letter = chr(i)
    filename = letter + ".txt"
    with open(filename, "w") as f:
        f.write("This is file %s.\n" % filename)