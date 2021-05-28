import art


print(art.logo)



def add(n1, n2):
    return n1 + n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

def sub(n1, n2):
    return n1 - n2

def calculator():
    n1 = float(input("What's the first number?: "))

    operations = {"+": add, "*": mult, "/": div, "-": sub}
    is_continue = True

    for symbol in operations:
            print(symbol)


    while is_continue == True:    
        operation_symbol = input("Pick the operation: " )
        n2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        input_design = input(f"Type 'y' continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if input_design =='y':
            n1 = answer
                
        else:
            is_continue = False
            calculator()



calculator()
