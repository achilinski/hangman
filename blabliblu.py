# calculator(1,2,3,4,5) -> 15
def multiply(*args, **kwargs):
    a = 1
    for i in args:
        a *= i
    return a


def calculator(*args, **kwargs):
    if args[-1] == '+':
        print(sum(args[:-1]))

    if args[-1] == '*':
        print(multiply(*args[:-1]))


print(multiply(4, 2, 3))