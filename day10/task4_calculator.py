# import art
#
# print(art.logo)
#
# number_1 = float(input("What's the first number?: "))
#
# def calculator(number_1, operator, number_2):
#     if operator == "+":
#         return  number_1 + number_2
#     elif operator == "-":
#         return  number_1 - number_2
#     elif operator == "*":
#         return  number_1 * number_2
#     elif operator == "/":
#         return  number_1 / number_2
#
# continued_calculate = True
# while continued_calculate:
#     print('''
#     +
#     -
#     *
#     /
#     ''')
#     operator = input("pick an operator:\n ")
#     number_2 = float(input("What's the next number?: "))
#     total_outcome = calculator(number_1, operator, number_2)
#     print(total_outcome)
#     continued = input(f"Type 'y' to continue calculating with {total_outcome}\n, "
#                       f"or type 'n' to start a new calculation: " )
#     if continued == "y":
#         number_1 = total_outcome
#     if continued == "n":
#         continued_calculate = False
#
# print(total_outcome)






def add(n1, n2):
    return n1 + n2
# my_favorite_operation = add
# print(my_favorite_operation(2, 3))
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operations ["*"](4,8))


def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: " )

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)

calculator() # recursion 递归