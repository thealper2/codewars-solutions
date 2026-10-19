class Router(object):
    def __init__(self):
        self.routes = {}
        
    def bind(self, path, method, action):
        self.routes[(path, method)] = action
        return self
    
    def runRequest(self, path, method):
        key = (path, method)
        if key in self.routes:
            return self.routes[key]()
        
        return 'Error 404: Not Found'