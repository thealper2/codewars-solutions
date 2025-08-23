def can_draw(shape: dict[str, list[str]]) -> bool:
    odd_degree_count = 0
    for vertex in shape:
        if len(shape[vertex]) % 2 != 0:
            odd_degree_count += 1
            
    return odd_degree_count == 0 or odd_degree_count == 2
