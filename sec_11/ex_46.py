def get_chars(a, path):
    with open(path, 'r') as myfile:
        content = myfile.read()

    cnt = content.count(a)
    return cnt

print(get_chars('a', "files/bear.txt"))