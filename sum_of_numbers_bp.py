def get_sum(a,b):
    
    response = sum(range(min(a,b), max(a,b)+1))
    print(response)
    return response

a = int(input("Please enter first number\n"))
b = int(input("Please enter second number\n"))

get_sum(a,b)