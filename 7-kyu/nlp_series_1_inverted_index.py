import re


def build_inverted_index(docs, term, case_sensitive, exact_match):
    result = []
    flags = 0 if case_sensitive else re.IGNORECASE
    if exact_match:
        pattern = r'(?<!\w)' + re.escape(term) + r'(?!\w)'
    else:
        pattern = re.escape(term)
        
    regex = re.compile(pattern, flags)
    for i, doc in enumerate(docs, start=1):
        if regex.search(doc):
            result.append(i)
            
    return result
