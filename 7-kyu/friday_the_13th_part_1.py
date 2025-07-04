def kill_count(counselors, jason):
    result = []
    for counselor in counselors:
        if counselor[1] < jason:
            result.append(counselor[0])
            
    return result
