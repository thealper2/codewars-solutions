def make_class(*attributes):
    def __init__(self, *args):
        if len(args) != len(attributes):
            raise ValueError(f"Expected {len(attributes)} arguments, got {len(args)}")
        for attr, arg in zip(attributes, args):
            setattr(self, attr, arg)
    
    cls = type('GeneratedClass', (), {'__init__': __init__})
    return cls