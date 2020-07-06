with open("files/bear1.txt", 'r') as bear1:
    b1 = bear1.read()

with open("files/bear2.txt", 'a+') as bear2:
    # bear2.read()
    bear2.write(b1)