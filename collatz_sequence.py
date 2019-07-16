def collatz(number):
    if number % 2 == 0:
        print(str(number) + " // 2 : ", number // 2)
        return number // 2
    else:
        print("collatz for ", number , " equals to ", (3*number)+1)
        return (3 * number) + 1

number = int(input("What number: \n"))

while number != 1:
    number = collatz(number)

print("Done")
