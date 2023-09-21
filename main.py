
from exeption import InvalidFormatExeption, InvalidNumberExeption, InvalidOperatorExeption, ZeroDivisionErrorNew
# import logic.parse
# import logic.calc
# import check_operator from logic.parse
from logic.parse import check_oprator
from logic.calc import add, subtract, multipy, divide


# main
while quit := input("Enter 3 with space [type 'quit or q' to Exit]: "):
    try:
        if quit.lower() == "quit" or quit.lower() == "q":
            break

        if len(quit.split(" ")) != 3:
            raise InvalidFormatExeption(
                1, "Please Enter right format [num1 operator num2] or enter 'q' to exit.")

        a, opr, b = quit.split(" ")
        if opr not in ["+", "-", "*", "/"]:
            raise InvalidOperatorExeption(
                2, "between number enter right operator ['+','-','*','/'] or enter 'q' to exit.")

        try:
            a = int(a)
            b = int(b)
        except ValueError:
            raise InvalidNumberExeption(3, "Enter number right")

        if b == 0:
            raise ZeroDivisionErrorNew(4, "Don't use 0 as second number to divide")


    except InvalidFormatExeption as ife:
        print(ife.msg)
    except InvalidNumberExeption as ine:
        print(ine.msg)
    except InvalidOperatorExeption as ioe:
        print(ioe.msg)
    except ZeroDivisionErrorNew as zden:
        print(zden.msg)
    else:
        print(check_oprator(opr, a, b))
