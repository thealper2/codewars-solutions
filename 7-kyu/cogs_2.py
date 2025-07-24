def cog_RPM(cogs, n):
    rpm1 = 1
    for i, w in enumerate(cogs[:n+1][::-1][:-1]):
        rpm1 *= -w / cogs[:n+1][::-1][i + 1]

    rpm2 = 1
    for i, w in enumerate(cogs[n:][:-1]):
        rpm2 *= -w / cogs[n:][i + 1]    

    return [rpm1, rpm2]
