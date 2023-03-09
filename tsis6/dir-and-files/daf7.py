with open("free.txt", "r") as source_file:
    with open("free2.txt", "w") as sec_file:
        sec_file.write(source_file.read())