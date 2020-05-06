class Node:
    def __init__(self, data, frequency):
        self.left = None
        self.right = None
        self.data = data
        self.frequency = frequency


    def printTree(self):
        print("Data: " + str(self.data) + "\t\t Frequency: " + str(self.frequency)),
        
        if self.left:
            self.left.printTree()
        
        if self.right:
            self.right.printTree()