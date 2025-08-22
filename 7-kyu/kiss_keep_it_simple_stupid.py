def is_kiss(words):
    words = words.split()
    n = len(words)
    for word in words:
        if len(word) > n:
            return "Keep It Simple Stupid"
        
    return "Good work Joe!"
    
