import re

def i_before_e(s):
    result = []
    last_index = 0

    for match_ in re.finditer(r'[ie]+', s):
        start, end = match_.start(), match_.end()
        seq = s[start:end]
        preceding = s[start - 1] if start > 0 else ''

        i_count = e_count = 0
        for c in seq:
            if c == 'i':
                i_count += 1
            elif c == 'e':
                e_count += 1

        result.append(s[last_index:start])

        if preceding == 'c':
            result.append('e' * e_count + 'i' * i_count)
        else:
            result.append('i' * i_count + 'e' * e_count)

        last_index = end

    result.append(s[last_index:])
    return ''.join(result)
