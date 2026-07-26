def zfc_definition(n: int) -> str:
    zfc = ['{}']
    for i in range(n):
        zfc.append('{' + ','.join(zfc) + '}')
        
    return zfc[-1]
