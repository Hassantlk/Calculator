def check_oprator(opr, a, b):
    dict_opr = {
        "+": add(a,b),
        "-": subtract(a,b),
        "*": multipy(a,b),
        "/": divide(a,b)
    }

    return dict_opr[opr]