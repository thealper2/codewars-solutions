def get_section_id(scroll, sizes):
    cumulative_size = 0
    for i, size in enumerate(sizes):
        if scroll < cumulative_size + size:
            return i

        cumulative_size += size

    return -1
