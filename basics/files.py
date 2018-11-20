address = ["Flat Floor Street", '18', 'New York']
pins = {'Mike':1234, 'Joe':1111, 'Jack':2222}

print(address[0], address[1])

pin = int(input('Enter your PIN:' ))

def find_in_file(f):
    myfile = open('sample.txt')
    fruits = myfile.read()
    print('fruits', fruits)
    fruits = fruits.splitlines()
    if f in fruits:
        return 'That fruit is in the list'
    else:
        return 'No such fruit!'

if pin in pins.values():
    fruit = input('Enter fruit: ')
    print(find_in_file(fruit))
else:
    print('Incorrect PIN"')
    print('This info can only be accessed by: ')
    for key in pins.keys():
        print(key)

