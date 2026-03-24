def breach_attempts(hackers, security_level, increase):
    total_breaches = 0
    for hacker in hackers:
        if hacker > security_level:
            total_breaches += 1
        else:
            security_level += increase
            
    return total_breaches
