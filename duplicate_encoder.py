#The goal of this exercise is to convert a string to a new string where each character in the new string 
# is "(" if that character appears only once in the original string, or ")" if that 
#character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encoder(word):
    word = word.upper()

    word_list = list(word)
    result = word_list.copy()
    
    for i in range(0 , len(word_list)):
        
        print(word_list[i])

        if word_list.count(word_list[i]) > 1 :
            result[i] = ")"

        else:
            result[i] = "("



def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

duplicate_encoder("Mimossa")
