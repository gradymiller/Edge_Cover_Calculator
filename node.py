



class Node:
    def __init__(self, nodes=[], edges=[], operator='*'):
        self.nodes = nodes
        self.edges = edges
        self.operator = operator
        self.children = []