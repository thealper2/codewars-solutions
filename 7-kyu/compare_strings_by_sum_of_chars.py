def compare(s1, s2):
    def process_string(s):
        if s is None:
            return ''
        if not isinstance(s, str):
            return ''
        if not s.isalpha():
            return ''
        return s.upper()
    
    s1_processed = process_string(s1)
    s2_processed = process_string(s2)
    
    sum1 = sum(ord(c) for c in s1_processed)
    sum2 = sum(ord(c) for c in s2_processed)
    
    return sum1 == sum2
