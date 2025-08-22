def wdm(talk):
    talk = talk.replace('puke', '')
    talk = talk.replace('hiccup', '')
    return ' '.join([word.strip() for word in talk.split()])
