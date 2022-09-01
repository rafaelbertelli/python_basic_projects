def add(a, b):
    result = a + b
    print_result(result)


def sub(a, b):
    result = a - b
    print_result(result)


def mult(a, b):
    result = a * b
    print_result(result)


def div(a, b):
    if a == 0 and b == 0:
        print("======= Não se divide com nada =======")
    else:
        result = a / b
        print_result(result)


def print_result(result):
    print("==============")
    print("RESULT: ", result)
    print("==============", "\n")


def calculator():
    print("~~~~~~~~~~~~~~")
    print("A => Addition")
    print("B => Subtration")
    print("C => Multiplication")
    print("D => Division")
    print("E => Exit")
    print("~~~~~~~~~~~~~~")

    choice = input("Enter your choice: ")

    try:
        if (choice == "A" or choice == 'a'):
            a = int(input("Type a number: "))
            b = int(input("Type another number: "))
            return add(a, b)
        elif (choice == "B" or choice == 'b'):
            a = int(input("Type a number: "))
            b = int(input("Type another number: "))
            return sub(a, b)
        elif (choice == "C" or choice == 'c'):
            a = int(input("Type a number: "))
            b = int(input("Type another number: "))
            return mult(a, b)
        elif (choice == "D" or choice == 'd'):
            a = int(input("Type a number: "))
            b = int(input("Type another number: "))
            return div(a, b)
        elif (choice == "E" or choice == 'e'):
            print("Exit")
            quit()

    except ValueError:
        print("======= Operações matemáticas somente com números!!! =======")
        return None
    except KeyboardInterrupt:
        print("======= Tchau =======")
        return None
    except:
        print("======= Errrrrrrrou =======")
        raise


def start():
    while True:
        calculator()


if __name__ == "__main__":
    start()
