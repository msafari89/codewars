Task

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct.
However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which will:

    Mask all digits (0-9) with #, unless they are first or last four characters.
    Never mask credit cards with less than 6 characters.
    Never mask non-digit characters.
Examples
Input 	Output 	Comments
"4556364607935616" 	"4###########5616" 	
"4556-3646-0793-5616" 	"4###-####-####-5616" 	
"64607935616" 	"6######5616" 	
ABCD-EFGH-IJKLM-NOPQ 	ABCD-EFGH-IJKLM-NOPQ 	
A1234567BCDEFG89HI 	A#######BCDEFG89HI 	
"12345" 	"12345" 	No #s if less than 6 characters
"" 	"" 	Make sure to handle empty strings
"Skippy" 	"Skippy"



def maskify(cc):
    #convert string to a list
    cc_split = list(cc)
    #calculate list length 
    cc_length = len(cc_split)
    #define digits in string format
    digits = ["0", "1","2","3","4","5","6","7","8","9"]
    
   
    if cc_length > 5:
        #avoid the last 4 character
        for i in range(cc_length - 4):
            #check for the first character
            if i == 0:
                cc = ''.join(cc_split)
            #check it it's a digit
            elif cc_split[i] in digits:
                cc_split[i] = "#"
                cc = ''.join(cc_split)

    return cc

maskify("AB231223235II22")