class FileNameExtractor:
    @staticmethod
    def extract_file_name(s):
        parts = s.split('_', 1)
        if len(parts) < 2:
            return ''
        
        name_with_ext = parts[1]
        last_dot_index = name_with_ext.rfind('.')
        if last_dot_index != -1:
            name_with_ext = name_with_ext[:last_dot_index]
            
        return name_with_ext
