M = 0
operands = ["+", "-", "*", "/"]
result = 0
x, y, = 0, 0


def is_one_digit(v):

    return -10 <= v < 10 and v == int(v)


def check(v1, v2, v3):

    msg = ""

    if is_one_digit(v1) and is_one_digit(v2):

        msg += " ... lazy"

    if (v1 == 1 or v2 == 1) and v3 == "*":

        msg += " ... very lazy"

    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):

        msg += " ... very, very lazy"

    if msg != "":

        msg = "You are" + msg

        print(msg)


while True:

    calc = input("Enter an equation\n")

    expression_list = calc.split(" ")

    try:

        if expression_list[0] == "M":

            x = M

            y = float(expression_list[2])

        elif expression_list[2] == "M":

            x = float(expression_list[0])

            y = M

        else:

            x = float(expression_list[0])

            y = float(expression_list[2])

    except ValueError:

        print("Do you even know what numbers are? Stay focused!")

    oper = expression_list[1]

    check(x, y, oper)

    if oper not in operands:

        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")

    else:

        if oper == "+":

            result = x + y

        elif oper == "-":

            result = x - y

        elif oper == "*":

            result = x * y

        elif oper == "/":

            if y == 0:

                print("Yeah... division by zero. Smart move...")

                continue

            else:

                result = x / y

        print(result)

        answer = input("Do you want to store the result? (y / n): ")

        M = 0

        if answer == "y":

            M = result

        continuation = input("Do you want to continue calculations? (y / n): ")

        if continuation == "y":

            continue

        elif continuation == "n":

            break
