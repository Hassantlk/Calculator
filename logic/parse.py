from logic.calc import *

def check_oprator(opr, a, b):
    dict_opr = {
        "/": divide(a,b),
        "+": add(a,b),
        "-": subtract(a,b),
        "*": multipy(a,b)
    }

    return dict_opr[opr]