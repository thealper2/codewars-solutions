def what_branch(time):
    hour, minute = map(int, time.split(':'))
    branches = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    index = (hour + 1) // 2 % 12
    return branches[index]
