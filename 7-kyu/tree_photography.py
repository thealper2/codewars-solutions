def tree_photography(trees):
    def visible_count(seq):
        count = 0
        max_height = 0
        for h in seq:
            if h > max_height:
                count += 1
                max_height = h
        return count
    
    left_count = visible_count(trees)
    right_count = visible_count(trees[::-1])
    return "left" if left_count >= right_count else "right"
