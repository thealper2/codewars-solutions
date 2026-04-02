def catalog(s, article):
    entries = s.strip().split('\n\n')
    results = []
    
    for entry in entries:
        if not entry.strip():
            continue
            
        name_start = entry.find('<name>') + 6
        name_end = entry.find('</name>')
        name = entry[name_start:name_end]
        
        if article in name:
            prx_start = entry.find('<prx>') + 5
            prx_end = entry.find('</prx>')
            price = entry[prx_start:prx_end]
            
            qty_start = entry.find('<qty>') + 5
            qty_end = entry.find('</qty>')
            quantity = entry[qty_start:qty_end]
            
            result_line = f"{name} > prx: ${price} qty: {quantity}"
            results.append(result_line)
            
    return '\r\n'.join(results) if results else 'Nothing'
