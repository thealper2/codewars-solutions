def are_equally_strong(your_left, your_right, friends_left, friends_right):
    your_strongest = max(your_left, your_right)
    your_weakest = min(your_left, your_right)
    friends_strongest = max(friends_left, friends_right)
    friends_weakest = min(friends_left, friends_right)
    return your_strongest == friends_strongest and your_weakest == friends_weakest
