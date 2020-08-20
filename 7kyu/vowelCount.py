def get_count(input_str):
    num_vowels = 0
    # count no. of vowels
    v='aeiou'
    for i in input_str:
        if i in v:
            num_vowels+=1
    
    return num_vowels