


def numbertoordinal(number):
    numstring = str(number)
    if number == 0 :
        return numstring
    if number in range(0, 10):
        last_digit = int(numstring[-1])

        if last_digit == 1:
            result = numstring + "st"
        elif last_digit == 2:
            result = numstring + "nd"
        elif last_digit == 3:
            result = numstring + "rd"
        else:
            result = numstring + "th"
    
    

    else:
        last_twodigit = int(numstring[-2:])
        last_digit = int(numstring[-1])

        if last_twodigit in range(10, 14):
            result = numstring + "th"
        else:
            if last_digit == 1:
                result = numstring + "st"
            elif last_digit == 2:
                result = numstring + "nd"
            elif last_digit == 3:
                result = numstring + "rd"
            else:
                result = numstring + "th"


    print(result)
    return result

numbertoordinal(0)
