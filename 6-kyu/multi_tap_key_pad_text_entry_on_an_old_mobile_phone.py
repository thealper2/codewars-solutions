def presses(phrase):
    keypad = ["1", "ABC2", "DEF3", "GHI4",
              "JKL5", "MNO6", "PQRS7", "TUV8",
              "WXYZ9", " 0", "*", "#"]
    
    chars = {}
    for key in keypad:
        for i, c in enumerate(key):
            chars[c] = i + 1
            
    total_presses = 0
    for c in phrase.upper():
        total_presses += chars.get(c, 0)
        
    return total_presses
