def Xbonacci(signature,n):
    #given a signature (list of integers) return n sequence. 
    #each element is the sum of last x elements.
    for i in range(n):
        signature.append(sum(signature[i:]))
        
    return signature[:n]