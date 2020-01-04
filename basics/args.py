def mean(*args):
    return sum(args) / len(args)
# print(mean(1, 3, 4))


def foo(*args):
    return sorted([s.upper() for s in args])
# print(foo("snow", "glacier", "icegerg"))


def max_kw(**kwargs):
    return max(kwargs)
print(max_kw(a = 1, b = 27, c = 3))
