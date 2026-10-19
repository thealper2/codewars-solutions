class FileMaster():
    def __init__(self, filepath):
        self.filepath = filepath
        
    def extension(self):
        name = self._filename_with_ext()
        idx = name.rfind('.')
        return name[idx + 1:] if idx != -1 else ''
    
    def filename(self):
        name = self._filename_with_ext()
        idx = name.rfind('.')
        return name[:idx] if idx != -1 else name
    
    def dirpath(self):
        idx = self.filepath.rfind('/')
        return self.filepath[:idx + 1] if idx != -1 else ''
    
    def _filename_with_ext(self):
        idx = self.filepath.rfind('/')
        return self.filepath[idx + 1:] if idx != -1 else self.filepath