def chuck_push_ups(st):
    print(st)
    if not isinstance(st, str):
        return 'FAIL!!'
    
    if not st:
        return 'CHUCK SMASH!!'
    
    numbers = []
    words = st.split()
    for word in words:
        n = len(word)
        number = ''
        for i in range(n):
            if word[i] in ['0', '1']:
                number += word[i]
                
        if number:
            numbers.append(int(number, 2))
            number = ''
    
    if not numbers:
        return 'CHUCK SMASH!!'
    
    return max(numbers)
