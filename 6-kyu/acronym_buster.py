def acronym_buster(text):
    acronyms = {
        'KPI': "key performance indicators",
        'EOD': "the end of the day", 
        'TBD': "to be decided",
        'WAH': "work at home",
        'IAM': "in a meeting",
        'OOO': "out of office",
        'NRN': "no reply necessary",
        'CTA': "call to action",
        'SWOT': "strengths, weaknesses, opportunities and threats"
    }
    
    words = []
    current_word = ""
    for char in text:
        if char.isalnum():
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ""
            words.append(char)
    if current_word:
        words.append(current_word)
    
    for i, word in enumerate(words):
        if len(word) >= 3 and word.isupper() and word.isalpha():
            if word not in acronyms:
                return f'{word} is an acronym. I do not like acronyms. Please remove them from your email.'
    
    result_words = []
    for word in words:
        if len(word) >= 3 and word.isupper() and word.isalpha() and word in acronyms:
            result_words.append(acronyms[word])
        else:
            result_words.append(word)
    
    result = "".join(result_words)
    sentences = result.split('. ')
    capitalized_sentences = []
    for sentence in sentences:
        if sentence:
            first_alpha_index = None
            for i, char in enumerate(sentence):
                if char.isalpha():
                    first_alpha_index = i
                    break
            
            if first_alpha_index is not None:
                capitalized = (sentence[:first_alpha_index] + 
                             sentence[first_alpha_index].upper() + 
                             sentence[first_alpha_index + 1:])
                capitalized_sentences.append(capitalized)
            else:
                capitalized_sentences.append(sentence)
        else:
            capitalized_sentences.append('')
    
    result = '. '.join(capitalized_sentences)
    return result
