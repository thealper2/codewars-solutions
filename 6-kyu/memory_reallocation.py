def mem_alloc(memory_banks: list[int]) -> int:
    seen = set()
    cycles = 0
    n = len(memory_banks)
    
    while tuple(memory_banks) not in seen:
        seen.add(tuple(memory_banks))
        max_blocks = max(memory_banks)
        index = memory_banks.index(max_blocks)
        blocks_to_redistribute = memory_banks[index]
        memory_banks[index] = 0
        
        for i in range(1, blocks_to_redistribute + 1):
            memory_banks[(index + i) % n] += 1
            
        cycles += 1
        
    return cycles
