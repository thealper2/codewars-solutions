class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        if not new_name[0].isupper() or not new_name.isalnum():
            raise Exception("Invalid class name")
        cls.__name__ = new_name
    
    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"
