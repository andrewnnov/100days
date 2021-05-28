import art


print(art.logo)

n1 = int(input("What's the first number?: "))


result = 0

def add(n1, n2):
    return n1 + n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

def sub(n1, n2):
    return n1 - n2

dict_operation = {"+": add, "*": mult, "/": div, "-": sub}

is_calc = True

while is_calc == True:
    
    operation = input("Pick the operation: + - * / : " )
    n2 = int(input("What's the second number?: "))

    if operation == "*":
        result = mult(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
    elif operation == "+":
        result = add(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
    elif operation == "-":
        result = sub(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
    elif operation == "/":
        result = div(n1, n2)
        print(f"{n1} {operation} {n2} = {result}")
    is_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation if you want to exit type 'ex': ")
    
    if is_continue == 'ex':
        is_calc = False    

    elif is_continue == 'y':
        n1 = result
    else:
        result = 0
        n1 = int(input("What's the first number?: "))
       
