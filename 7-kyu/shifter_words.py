def shifter(s):
    valid = set("HINOSXZMW")
    words = s.split()
    seen = set()
    for word in words:
        if all(c in valid for c in word):
            seen.add(word)
            
    return len(seen)
