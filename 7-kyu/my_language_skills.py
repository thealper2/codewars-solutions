def my_languages(results):
    filtered = {lang: score for lang, score in results.items() if score >= 60}
    score_lang = [(score, lang) for lang, score in filtered.items()]
    n = len(score_lang)

    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if score_lang[j][0] > score_lang[max_idx][0]:
                max_idx = j
        score_lang[i], score_lang[max_idx] = score_lang[max_idx], score_lang[i]
    
    sorted_languages = [lang for score, lang in score_lang]
    return sorted_languages