def count_smileys(arr):
    count = 0
    for face in arr:
        if len(face) in (2, 3) and face[0] in ':;':
            if len(face) == 2:
                if face[1] in ')D':
                    count += 1
            else:
                if face[1] in '-~' and face[2] in ')D':
                    count += 1
                    
    return count