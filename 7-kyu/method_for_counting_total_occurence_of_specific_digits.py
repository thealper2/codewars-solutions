class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        all_digits = []
        for num in integers_list:
            num = abs(num)
            if num == 0:
                all_digits.append(0)
            else:
                while num > 0:
                    all_digits.append(num % 10)
                    num = num // 10
        
        digit_counts = {}
        for digit in all_digits:
            if digit in digit_counts:
                digit_counts[digit] += 1
            else:
                digit_counts[digit] = 1

        result = []
        for digit in digits_list:
            count = digit_counts.get(digit, 0)
            result.append((digit, count))
        
        return result