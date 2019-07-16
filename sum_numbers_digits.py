def sumDigits(number):
    string_number = [int(d) for d in str(abs(number))]
    return sum(string_number)

print(sumDigits(892))
