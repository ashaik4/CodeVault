# Union find class 
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]  # Initialize each node's root to itself
    

    def find(self, x):
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if (rootX != rootY):
            for i in range(len(self.root)):
                if self.root[i] == rootX:
                    self.root[i] = rootY
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)
