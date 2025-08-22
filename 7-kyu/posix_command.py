import os

def get_output(s):
    result = os.popen(s).read()
    return result
