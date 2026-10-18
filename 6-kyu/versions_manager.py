class VersionManager:
    def __init__(self, version='0.0.1'):
        if version == '':
            version = '0.0.1'
        
        self.history = []
        parts = version.split('.')
        nums = []
        
        for i in range(3):
            if i < len(parts) and parts[i] != '':
                try:
                    nums.append(int(parts[i]))
                except ValueError:
                    raise Exception('Error occured while parsing version!')
            else:
                nums.append(0)
                
        self.major_v, self.minor_v, self.patch_v = nums
        
    def major(self):
        self.history.append((self.major_v, self.minor_v, self.patch_v))
        self.major_v += 1
        self.minor_v = 0
        self.patch_v = 0
        return self
    
    def minor(self):
        self.history.append((self.major_v, self.minor_v, self.patch_v))
        self.minor_v += 1
        self.patch_v = 0
        return self
    
    def patch(self):
        self.history.append((self.major_v, self.minor_v, self.patch_v))
        self.patch_v += 1
        return self
    
    def rollback(self):
        if not self.history:
            raise Exception('Cannot rollback!')
            
        self.major_v, self.minor_v, self.patch_v = self.history.pop()
        return self
    
    def release(self):
        return f'{self.major_v}.{self.minor_v}.{self.patch_v}'