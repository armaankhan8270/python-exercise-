import re


def number(x):
    if (x < 100):
        print("number is in range of 100")
    elif (100 < x < 1000):
        print("number is in range of 1000")
    elif (1000 < x < 2000):
        print("number is in range of 2000")


number(99)
number(1099)
number(199)
