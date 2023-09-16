import exeption
import logic.parse
import parse
import logic.calc
import calc

# exeption
class InvalidFormatExeption(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    
    
    def __str__(self):
        return f"{self.code} Number: {self.msg}"

class InvalidNumberExeption(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    
    
    def __str__(self):
        return f"{self.code} Number: {self.msg}"

class InvalidOperatorExeption(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
    
    
    def __str__(self):
        return f"{self.code} Number: {self.msg}"








# parse
def check_oprator(opr, a, b):
    dict_opr = {
        "+": add(a,b),
        "-": subtract(a,b),
        "*": multipy(a,b),
        "/": divide(a,b)
    }

    return dict_opr[opr]

#calc
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multipy(a, b):
    return a * b

def divide(a, b):
    return a/b

# main
while quit:= input("Enter 3 with space [type 'quit or q' to Exit]: "):
    try:
        if quit.lower() == "quit" or quit.lower() == "q":
            break

        if len(quit.split(" ")) != 3:
            raise InvalidFormatExeption(1, "Please Enter right format [num1 operator num2] or enter 'q' to exit.")

        a, opr, b = quit.split(" ")
        if opr not in ["+","-","*","/"]:
            raise InvalidOperatorExeption(2, "between number enter right operator ['+','-','*','/'] or enter 'q' to exit.")

        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise InvalidNumberExeption(3,"Enter number right")

    except InvalidFormatExeption as ife:
        print(ife.msg)
    except InvalidNumberExeption as ine:
        print(ine.msg)
    except InvalidOperatorExeption as ioe:
        print(ioe.msg)
    else:
        print(check_oprator(opr, a, b))


