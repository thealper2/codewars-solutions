from collections import Counter

def is_anagram(test, original):
    c_test = Counter(test.lower())
    c_orig = Counter(original.lower())
    
    for k in c_test.keys():
        if c_test[k] != c_orig[k]:
            return False
        
    for k in c_orig.keys():
        if c_orig[k] != c_test[k]:
            return False
        
    return True
