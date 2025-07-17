def evil_code_medal(user_time, gold, silver, bronze):
    def time_to_seconds(time_str):
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s
    
    user_sec = time_to_seconds(user_time)
    gold_sec = time_to_seconds(gold)
    silver_sec = time_to_seconds(silver)
    bronze_sec = time_to_seconds(bronze)
    
    if user_sec < gold_sec:
        return "Gold"
    elif user_sec < silver_sec:
        return "Silver"
    elif user_sec < bronze_sec:
        return "Bronze"
    else:
        return "None"
