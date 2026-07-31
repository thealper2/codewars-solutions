from fractions import Fraction as F

def rake_and_burn(days):
    yard = F(0)
    pile = F(0)
    count = 0
    rained_yesterday = False

    for precip, wind, direction in days:
        if precip == 'snow':
            break

        raining = (precip == 'rain')
        bad_burn_dir = direction in ('SW', 'S', 'SE')

        can_burn = (not raining and not rained_yesterday
                    and wind <= 10 and not bad_burn_dir)

        if pile == 1:
            if can_burn:
                pile = F(0)
                yard += F(1, 4)
                if yard >= 1:
                    count += 1
                    yard -= 1
        else:
            if not raining and not rained_yesterday and wind <= 12:
                yard += F(1, 3)
                pile += F(1, 2)
                if yard >= 1:
                    count += 1
                    yard -= 1

        rained_yesterday = raining

    return count
