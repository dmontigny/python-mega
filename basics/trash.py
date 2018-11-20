path = 'C:\\Users\\e147645\\PycharmProjects\\python-mega\\basics\\'

myfile = open(path + 'emps2.txt', 'w')
nums = [1, 2, 3]
for i in nums:
    print(i)
    myfile.write(str(i) + "\n")

myfile.close()


