from numpy import outer


def histogram(format, character):
    for i in format:
        result = i*character
        print(result)


histogram([1, 4, 5, 6, 7, 8], '*')
