class List:
    def __init__(self, data_type):
        self.data_type = data_type
        self.items = []
        self.count = 0
    
    def add(self, item):
        if not isinstance(item, self.data_type):
            type_name = self.data_type.__name__
            return f"This item is not of type: {type_name}"
        self.items.append(item)
        self.count += 1
        return self