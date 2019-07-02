#Usually when you buy something, you're asked whether your credit card number, 
# phone number or answer to your most secret question is still correct. 
# However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

#Your task is to write a function maskify, which changes all but the last four characters into '#'.

def maskify(cc):
    
    cc_split = list(cc)
    cc_length = len(cc_split)
    if cc_length >= 5:
        for i in range(0, cc_length-4):
            cc_split[i] = "#"
            cc = ''.join(cc_split)
        print(cc)
    else:
        print(cc)
        return cc

maskify("SF$SDfgsd2eA")