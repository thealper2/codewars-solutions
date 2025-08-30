def block_player(a, b):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for win in wins:
        if a in win and b in win:
            for num in win:
                if num != a and num != b:
                    return num
