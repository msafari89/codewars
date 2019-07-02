#    Instruction

# Given two integers a and b, which can be positive or negative, 
# find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

def get_sum(a,b):
    if a == b:
        return a
    elif a > b:
        min_number = b
        max_number = a
    else:
        min_number = a
        max_number = b

    numbers_list = range(min_number, max_number+1)
    total_sum = 0
    for i in numbers_list:
        total_sum = i + total_sum
    
    print("Total sum is ", total_sum)
    return total_sum

a = int(input("Please enter first number\n"))
b = int(input("Please enter second number\n"))

get_sum(a,b)



####################### Best Practice Solution ########################

def get_sum(a,b)
    return 
