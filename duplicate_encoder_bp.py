#Understanding list comprehension: https://medium.com/better-programming/list-comprehension-in-python-8895a785550b
#List comprehension: https://www.machinelearningplus.com/python/list-comprehensions-in-python/

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
