def comment(text, language):
    lines = text.split('\n')
    formatted_lines = []
    
    if language == 'Bash':
        prefix = '# '
        formatted_lines = [prefix + line for line in lines]
    elif language == 'Bash Multiline':
        formatted_lines = [': "'] + lines + ['"']
    elif language == 'Python':
        prefix = '# '
        formatted_lines = [prefix + line for line in lines]
    elif language == 'Python Multiline':
        formatted_lines = ['"""'] + lines + ['"""']
    elif language == 'Javascript':
        prefix = '// '
        formatted_lines = [prefix + line for line in lines]
    elif language == 'Javascript Multiline':
        formatted_lines = ['/*'] + lines + ['*/']
    elif language == 'SQL':
        prefix = '-- '
        formatted_lines = [prefix + line for line in lines]
    elif language == 'JavaDoc':
        formatted_lines = ['/**'] + ['* ' + line for line in lines] + ['*/']
    elif language == 'SGML':
        formatted_lines = ['<!-- ' + line + ' -->' for line in lines]
    
    return '\n'.join(formatted_lines)
