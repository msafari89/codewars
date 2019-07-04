#Write Number in Expanded Form

#You will be given a number and you will need to return it as a string in Expanded Form. For example:

#expanded_form(12) # Should return '10 + 2'
#expanded_form(42) # Should return '40 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'

#NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    digits = [int(i) for i in str(num)]
    digits.reverse()
    result = []
    final = ""

    for idx, val in enumerate(digits):
        positional_value = 10 ** idx
        if val != 0 :
            value = val * positional_value
            result.append(value)
    
    result.reverse()

    for r in result:
        if r == result[-1]:
            final = final + str(r)
        else:
            final = final + str(r) + " + "
    print(final)
    return final


def expanded_form2(num):
    num = str(num)
    st = ''
    for j, i in enumerate(num):
        if i != '0':
            st += ' + {}{}'.format(i, (len(num[j+1:])*'0'))
    return st.strip(' +')




expanded_form(145067821234)


