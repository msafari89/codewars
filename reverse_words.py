#Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in the string should be retained.

#"This is an example!" ==> "sihT si na !elpmaxe"
#"double  spaces"      ==> "elbuod  secaps"

def reverse_word(word):
    #print("".join(reversed(word)))
    word_list = word.split(" ")    
    elements = ["".join(reversed(elm)) for elm in word_list ]
    elements = " ".join(elements)

    return elements


reverse_word("Masoud Safari  Double Spaced")

