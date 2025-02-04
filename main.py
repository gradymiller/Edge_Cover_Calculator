##from identifier import Identifier
#from selector import Selector
#from lemma import split_edges
#import networkx as nx




def main():
    pass
    # Base case: when there are all path graphs
    # Increment: doing the lemma to simplify down

    







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





