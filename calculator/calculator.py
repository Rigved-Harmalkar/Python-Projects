def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
              "+": add, 
              "-": subtract,
              "*":multiply,
              "/":divide}
def calculator():
    num1 = float(input("Enter first number: "))
    for operator in operations:
        print(operator)
    calc = True
    while calc:
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("Enter second number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input("Do you wanna continue? Type yes or no: ").lower == "yes":
            num1 = answer
        else:
            calc = False
            calculator()
        
    






