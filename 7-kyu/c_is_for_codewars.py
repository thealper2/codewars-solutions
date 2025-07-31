def generate_C(size):
    top_bottom_line = "C" * (5 * size)
    middle_line = "C" * size

    top_section = [top_bottom_line for _ in range(size)]
    middle_section = [middle_line for _ in range(3 * size)]
    bottom_section = [top_bottom_line for _ in range(size)]

    all_lines = top_section + middle_section + bottom_section
    result = "\n".join(all_lines)
    return result
