from preloaded import Like, Dislike, Nothing


def like_or_dislike(lst):
    state = Nothing
    for action in lst:
        if state == action:
            state = Nothing
        else:
            state = action
            
    return state