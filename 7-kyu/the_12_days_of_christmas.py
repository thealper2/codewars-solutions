def song_sorter(lines):
    day_line = None
    gift_lines = []
    partridge_line = None
    
    for line in lines:
        if line.startswith('On the ') and 'day of Christmas my true love gave to me' in line:
            day_line = line
        elif line == 'a partridge in a pear tree.':
            partridge_line = line
        else:
            gift_lines.append(line)
    
    def get_gift_number(gift_line):
        first_word = gift_line.split()[0]
        num_str = ''.join(filter(str.isdigit, first_word))
        return int(num_str) if num_str else 0
    
    gift_lines_sorted = sorted(gift_lines, key=get_gift_number, reverse=True)
    sorted_lines = [day_line] + gift_lines_sorted
    if partridge_line:
        sorted_lines.append(partridge_line)
    
    return sorted_lines