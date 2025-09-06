def fifo(n, reference_list):
    i = 0
    memory = [-1 for _ in range(n)]
    for item in reference_list:
        if item in memory:
            continue
            
        if len(memory) < n:
            memory.append(item)
        elif len(memory) == n:
            memory[i % n] = item
            
        i += 1
            
    return memory
