def circle_mender(content: str) -> str:
    result = []
    for line in content.split('\n'):
        l = line.find('#')
        r = line.rfind('#')
        if l != -1 and r != -1:
            line = line[:l] + '#' * (r - l + 1) + line[r+1:]
        
        result.append(line)
        
    return '\n'.join(result)
