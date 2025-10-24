import os

def create_file_dict():
    result = {}
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    result[filename] = first_line + '\n'
                    
            except (IOError, UnicodeDecodeError):
                continue
                
    return result
