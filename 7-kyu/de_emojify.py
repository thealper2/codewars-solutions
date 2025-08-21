def deemojify(s):
    emote_map = {
        ":)": "0",
        ":D": "1",
        ">(": "2",
        ">:C": "3",
        ":/": "4",
        ":|": "5",
        ":O": "6",
        ";)": "7",
        "^.^": "8",
        ":(": "9"
    }
    
    chains = s.split("  ")
    result = []
    
    for chain in chains:
        emotes = chain.split()
        digits = []
        for emote in emotes:
            digits.append(emote_map[emote])
        
        ascii_code = int(''.join(digits))
        result.append(chr(ascii_code))
    
    return ''.join(result)
