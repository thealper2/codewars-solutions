def get_root_property(dict_, target):
    for key, value in dict_.items():
        if isinstance(value, list):
            if target in value:
                return key
        else:
            result = get_root_property(value, target)
            if result is not None:
                return key

    return None
