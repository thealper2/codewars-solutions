def find_nth_occurrence(substring, string, occurrence=1):
    len_substring = len(substring)
    len_string = len(string)
    count = 0

    for i in range(len_string - len_substring + 1):
        if string[i : i + len_substring] == substring:
            count += 1
            if count == occurrence:
                return i

    return -1
