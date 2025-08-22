class Tree:
    def __init__(self, trunks):
        self.trunks = trunks
        self.branches = trunks * 10
        self.twigs = trunks * 100
        self.leaves = trunks * 1000
    
    def chop_trunk(self, n):
        n = min(n, self.trunks)
        if n > 0:
            self.trunks -= n
            self.chop_branch(n * 10)
    
    def chop_branch(self, n):
        n = min(n, self.branches)
        if n > 0:
            self.branches -= n
            self.chop_twig(n * 10)
    
    def chop_twig(self, n):
        n = min(n, self.twigs)
        if n > 0:
            self.twigs -= n
            self.chop_leaf(n * 10)
    
    def chop_leaf(self, n):
        n = min(n, self.leaves)
        self.leaves -= n
    
    def describe(self):
        return f"This tree has {self.trunks} trunks, {self.branches} branches, {self.twigs} twigs and {self.leaves} leaves."
