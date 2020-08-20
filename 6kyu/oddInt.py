import collections
def find_it(seq):
    #to find the integer that appears an odd number of times
    freq={}
    for i in seq:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    for i in freq:
        if freq[i]%2 !=0:
            return i