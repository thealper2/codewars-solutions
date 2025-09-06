def find_page_number(pages):
    n = len(pages)
    result = []
    c = 0
    for i, page in enumerate(pages, start=1):
        if i - c != page:
            result.append(page)
            c += 1
    
    return result
