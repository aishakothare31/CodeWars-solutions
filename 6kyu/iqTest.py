def iq_test(numbers):
    #determine which no. differs from others and return its index (starts from 1 not 0)
    n=numbers.split()
    l=[int(i)%2==0 for i in n]
    return l.index(True)+1 if l.count(True) ==1 else l.index(False)+1
