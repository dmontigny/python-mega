with open("files/veggies.txt", 'w') as myfile:
    myfile.write("tomato\nonion\ncarrot\n")
    myfile.write("garlic\n")

with open("files/veggies.txt", 'r') as myread:
    content = myread.read()

print(content)



