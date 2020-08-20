import string

def is_pangram(s):
    #a pangram consist of all alphabets atleast once in a sentence
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in s:
        if i in punctuations:
            s=s.replace(i,'')
    alpha=set(string.ascii_lowercase)
    return True if alpha<=set((s.lower())) else False