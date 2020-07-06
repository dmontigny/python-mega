content = ''

with open("files/data.txt", 'r') as mydata:
    content = mydata.read()

with open("files/data.txt", 'a+') as mydata:
    mydata.write("\n{}".format(content) * 2)
