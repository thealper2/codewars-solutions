def triple_crown(receivers):
    names = list(receivers.keys())

    yards = {}
    touchdowns = {}
    receptions = {}

    for name in names:
        stats = receivers[name]
        yards[name] = stats["Receiving yards"]
        touchdowns[name] = stats["Receiving touchdowns"]
        receptions[name] = stats["Receptions"]

    def get_leader(stats_dict):
        max_val = max(stats_dict.values())
        leaders = [name for name, val in stats_dict.items() if val == max_val]
        return leaders if len(leaders) == 1 else None

    yards_leader = get_leader(yards)
    touchdowns_leader = get_leader(touchdowns)
    receptions_leader = get_leader(receptions)

    if (
        yards_leader
        and touchdowns_leader
        and receptions_leader
        and yards_leader[0] == touchdowns_leader[0] == receptions_leader[0]
    ):
        return yards_leader[0]
    else:
        return "None of them"
