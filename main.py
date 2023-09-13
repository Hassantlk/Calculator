import exeption
import logic.parse
import parse
import logic.calc
import calc

def check_oprator(opr, a, b):
    dict_opr = {
        "+": add(a,b),
        "-": subtract(a,b),
        "*": multipy(a,b),
        "/": divide(a,b)
    }

    return dict_opr[opr]


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multipy(a, b):
    return a * b

def divide(a, b):
    return a/b


a, opr, b = input("Enter 3 with space: ").split(" ")
a = int(a)
b = int(b)

print(check_oprator(opr, a, b))

