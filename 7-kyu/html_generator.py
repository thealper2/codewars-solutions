class HTMLGen:
    def __init__(self):
        pass
    
    def a(self, text):
        return '<a>' + text + '</a>'
    
    def b(self, text):
        return '<b>' + text + '</b>'
    
    def p(self, text):
        return '<p>' + text + '</p>'
    
    def body(self, text):
        return '<body>' + text + '</body>'
    
    def div(self, text):
        return '<div>' + text + '</div>'
    
    def span(self, text):
        return '<span>' + text + '</span>'
    
    def title(self, text):
        return '<title>' + text + '</title>'
    
    def comment(self, text):
        return '<!--' + text + '-->'
