def generate_markdowns(markdown, text, url_or_language):
    if markdown == 'link':
        return f'[{text}]({url_or_language})'
    elif markdown == 'img':
        return f'![{text}]({url_or_language})'
    elif markdown == 'code':
        return f"```{url_or_language}\n{text}\n```"
    else:
        return ''
