def histogram(results):
    n = len(results)
    total = sum(results)
    result = []
    
    for i in range(n - 1, -1, -1):
        if results[i]:
            percentage = results[i] / total
            num_bars = int(50 * percentage)
            line = f"{i + 1}|{'█' * num_bars} {int(percentage * 100)}%"
            result.append(line)
        else:
            line = f"{i + 1}|"
            result.append(line)
            
    return "\n".join(result) + '\n'