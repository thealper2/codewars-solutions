def communication_module(packet):
    header = packet[:4]
    instruction = packet[4:8]
    data1 = int(packet[8:12])
    data2 = int(packet[12:16])
    footer = packet[16:20]
    
    if instruction == "0F12":
        result = data1 + data2
    elif instruction == "B7A2":
        result = data1 - data2
    elif instruction == "C3D9":
        result = data1 * data2
    else:
        result = 0
    
    if result < 0:
        result = 0
    elif result > 9999:
        result = 9999
    
    result_str = str(result).zfill(4)
    return f"{header}FFFF{result_str}0000{footer}"
