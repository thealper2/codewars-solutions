def proofread(st):
    lower = st.lower()
    fixed = lower.replace('ie', 'ei')

    sentences = fixed.split('.')
    result = []
    for sent in sentences:
        i = 0
        while i < len(sent) and not sent[i].isalpha():
            i += 1
        if i < len(sent):
            result.append(sent[:i] + sent[i].upper() + sent[i + 1:])
        else:
            result.append(sent)
            
    return '.'.join(result)