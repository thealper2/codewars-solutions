def expected_party_rank(voteA, voteB, swingA, swingB):
    voteC_last = 100 - voteA - voteB
    new_voteA = voteA + swingA
    new_voteB = voteB + swingB
    new_voteA = max(0, min(new_voteA, 100))
    new_voteB = max(0, min(new_voteB, 100))
    new_voteC = 100 - new_voteA - new_voteB
    new_voteC = max(0, min(new_voteC, 100))
    parties = [
        ('A', new_voteA),
        ('B', new_voteB),
        ('C', new_voteC)
    ]
    parties.sort(key=lambda x: (-x[1], x[0]))
    result = [party[0] for party in parties]
    return result
