def is_valid_walk(walk):
    #determine if walk is valid
    return len(walk)==10 and walk.count('n')==walk.count('s') and walk.count('w')==walk.count('e')