import ast


def calc_pol(pol_str, x = None):
    if x is None:
        return 'There is no value for x'
    
    node = ast.parse(pol_str, mode='eval')
    code_object = compile(node, filename='<string>', mode='eval')
    result = eval(code_object, {'x': x})
    
    if result == 0:
        return f'Result = 0, so {x} is a root of {pol_str}'
    else:
        return f'Result = {result}'
