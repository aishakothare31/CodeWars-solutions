def open_or_senior(data):
    # to be a senior, be atleast 55 or more and have exp of more than 7 yrs.
    mem = []
    for member in data:
        if member[0]>=55 and member[1]>7:
            mem.append('Senior')
        else:
            mem.append('Open')
    return mem