def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(0))
except ZeroDivisionError as error:
    print('Error: Invalid argument: ' + str(error))
