def omit_hashtag(message, hashtag):
    pos = message.find(hashtag)
    if pos == -1:
        return message
    
    return message[:pos] + message[pos + len(hashtag):]
