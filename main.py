##from identifier import Identifier
#from selector import Selector
#from lemma import split_edges
#import networkx as nx

class Node:
    def __init__(self, signature, nodes=[], edges=[], operator='*'):
        self.signature = signature
        self.nodes = nodes
        self.edges = edges
        self.operator = operator
        self.children = []

    def __repr__(self):
        return str(self.signature)
    
    def set_nodes(self):
        pass

    def set_edges(self):
        pass
    
    def run_lemma(self):
        self.operator = '*'
        pass # Return -> case with e, case without e (Run Identifier() on both cases)

    def make_children(self):
        case1, case2 = [[[],[]],[[],[]]], [[[],[]],[[],[]]] # This is temporary because I haven't made the run_lemma() function
        # yellow = each case, pink = paths/non-paths, blue = graph piece
        for case in case1:
            for c in case:
                pass
                
        



    



graph =[[(1, 2), (1, 4), (4, 3), (3, 2)]]
node_list = [ Node(i) for i in range(len(graph))]



def path_graph_evaluator(graph):
    n = len(graph)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, int(n) + 1):
            a, b = b, a + b
        return b






