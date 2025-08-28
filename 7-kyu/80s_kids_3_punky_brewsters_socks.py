def get_socks(name, socks):
    if name == 'Punky':
        seen = set()
        for sock in socks:
            if sock in seen:
                continue
                
            seen.add(sock)
            if len(seen) == 2:
                return list(seen)
            
        return []
    
    else:
        count = {}
        for sock in socks:
            if sock not in count:
                count[sock] = 1
            else:
                count[sock] += 1
                if count[sock] == 2:
                    return [sock, sock]
                
        return []
            
