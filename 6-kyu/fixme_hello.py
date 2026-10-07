class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
        self._order = []
        
    def _track(self, attr):
        if attr not in self._order:
            self._order.append(attr)
    
    def setAge(self, age):
        self.age = age
        self._track('age')
        return self
        
    def setSex(self, sex):
        self.sex = sex
        self._track('sex')
        return self
        
    def setName(self, name):
        self.name = name
        self._track('name')
        return self
        
    def hello(self):
        result = ['Hello.']
        for attr in self._order:
            if attr == 'age':
                result.append(f'I am {self.age}.')
                
            elif attr == 'sex':
                result.append(f'I am {"female" if self.sex == "F" else "male"}.')
            
            elif attr == 'name':
                result.append(f'My name is {self.name}.')
        
        return ' '.join(result)