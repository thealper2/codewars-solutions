def pass_the_bill(total_members, conservative_party_members, reformist_party_members):
    independents = total_members - conservative_party_members - reformist_party_members
    required = (total_members // 2) + 1

    if conservative_party_members >= required:
        return 0

    needed = required - conservative_party_members
    if needed <= independents and needed >= 0:
        return needed
    else:
        return -1
