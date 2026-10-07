import re


def highlight(code):
    colors = {'F': 'pink', 'L': 'red', 'R': 'green'}
    def replace(m):
        c = m.group(0)[0]
        if c in colors:
            return f'<span style="color: {colors[c]}">{m.group(0)}</span>'
        else:
            return f'<span style="color: orange">{m.group(0)}</span>'

    return re.sub(r'F+|L+|R+|\d+', replace, code)