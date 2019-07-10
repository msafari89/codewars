def calculate(expression):
    # define operations with two arguments
    operations = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b)
            }

    # convert to list
    elements = expression.split()
    # define working
    working = []
    # return 0 if string is empty
    if len(elements) == 0:
        return 0

    for element in elements:
        # Get the last two members of working
        if element in operations:

            arg2 = working.pop()
            arg1 = working.pop()
            # calculate results for this step
            result = operations[element](arg1, arg2)
            working.append(result)
        # convert numbers to float and add to working
        else:
            working.append(float(element))

    return working.pop()

calculate("8 10 +")
