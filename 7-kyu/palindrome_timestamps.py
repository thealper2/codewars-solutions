def palindrome_time(lst):
    def is_palindrome(h, m, s):
        time_str = f"{h:02d}{m:02d}{s:02d}"
        return time_str == time_str[::-1]
    
    count = 0
    h1, m1, s1, h2, m2, s2 = lst
    current_h = h1
    current_m = m1
    current_s = s1
    while (current_h, current_m, current_s) <= (h2, m2, s2):
        if is_palindrome(current_h, current_m, current_s):
            count += 1
            
        current_s += 1
        if current_s == 60:
            current_m += 1
            current_s = 0
            
        if current_m == 60:
            current_h += 1
            current_m = 0
            
    return count
            
