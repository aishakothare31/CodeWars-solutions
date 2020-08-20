import collections
def is_isogram(string):
    #a string having no consecutive or non consecutive repeating letters
    if len(string.lower()) == len(set(string.lower())):
        return True
    else:
        return False