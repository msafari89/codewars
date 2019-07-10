
def calculate(expression):

    operations = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b)
            }

    elements = expression.split()
    working = []
    for element in elements:
        if element in operations:


            arg2 = working.pop()
            arg1 = working.pop()
            result = operations[element](arg1, arg2)
            working.append(result)

        else:
            working.append(float(element))
    
    return working.pop()

print(calculate("5 1 2 + 4 * + 3 -"))
