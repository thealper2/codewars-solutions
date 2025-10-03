def wordify(n):
    ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
            'seventeen', 'eighteen', 'nineteen']
    
    tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    if n == 0:
        return 'zero'
    
    result = []
    if n >= 100:
        result.append(ones[n // 100])
        result.append('hundred')
        n %= 100
        
    if n >= 20:
        result.append(tens[n // 10])
        if n % 10 != 0:
            result.append(ones[n % 10])
            
    elif n > 0:
        result.append(ones[n])
        
    return ' '.join(result)
