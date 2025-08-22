def find_variable():
    for name, value in globals().items():
        if value == 777:
            return name
        
    for name, value in locals().items():
        if value == 777:
            return name
