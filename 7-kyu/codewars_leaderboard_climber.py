def leader_b(user, user_score, your_score):
    if user_score == your_score:
        return "Only need one!"
    elif user_score < your_score:
        return "Winning!"
    else:
        diff = user_score - your_score
        beta_kata = diff // 3
        eight_kyu_kata = diff % 3
        return f"To beat {user}'s score, I must complete {beta_kata} Beta kata and {eight_kyu_kata} 8kyu kata.{' Dammit!' if beta_kata >= 1000 else ''}"
