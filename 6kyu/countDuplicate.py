import collections
def duplicate_count(text):
    # return distinct case insensitive alphabets and digits that occcur more than once
    t=dict(collections.Counter(text.lower()))
    t= {k:val for k,val in t.items() if val>1 }
    return len(t)