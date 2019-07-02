#Trolls are attacking your comment section!

#A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

#Your task is to write a function that takes a string and return a new string with all vowels removed.

#For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

#Note: for this kata y isn't considered a vowel.


############# Tips #############
# ord() returns a integer representing unicode
# use dictionary.fromkeys method to generate dictionary using specified keys and values:
    # example: dictionary.fromkeys(keys, values)

# help here : https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python

def disemvowl(string):
    tran_table = dict.fromkeys(map(ord, 'aeiouAEIOU'), None)
    result = string.translate(tran_table)
    print(result)
    return result   

string = str(input("Please enter the string\n"))
disemvowl(string)