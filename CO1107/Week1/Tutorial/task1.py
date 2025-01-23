# Task 1: 
# Write a function letter_counter that takes in a word and returns a 
# tuple formed by a histogram (a set of frequencies for all the 
# letters in the word) and the total number of letters in the word.

def letter_counter(word):
    
    d = {}
    
    for c in word:
        if c not in d:
            d[c] = 1
        else: 
            d[c] += 1
    keys = list(d.keys())
    count = 0
    
    for k in keys:
        count += d[k]
    return (d,count)

