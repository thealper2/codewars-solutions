def create_template(template):
    def fill(**data):
        result = template
        start = 0
        while True:
            start = result.find('{{', start)
            if start == -1:
                break
                
            end = result.find('}}', start)
            if end == -1:
                break
                
            key = result[start+2:end].strip()
            value = data.get(key, '')
            result = result[:start] + value + result[end+2:]
            start += len(value)
            
        return result
    
    return fill
