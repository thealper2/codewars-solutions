def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    
    longest = ""
    for i in range(n - k + 1):
        current_combined = "".join(strarr[i:i+k])
        
        if len(current_combined) > len(longest):
            longest = current_combined
            
    return longest