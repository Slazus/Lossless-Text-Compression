class Node:
    def __init__(self, data, frequency):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.frequency = frequency

    def addParent(self, node):
        self.parent = node
        if not self.parent.left:
            self.parent.left = self
        else:
            self.parent.right = self

    def PrintTree(self):
        print("Data: " + str(self.data) + "\t\t Frequency: " + str(self.frequency)),
        
        if self.left:
            self.left.PrintTree()
        
        if self.right:
            self.right.PrintTree()