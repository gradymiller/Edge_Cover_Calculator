from identifier import Identifier
from selector import Selector
from lemma import split_edges
import networkx as nx

class Node:
    def __init__(self, nodes=[], edges=[], operator='*'):
        self.operator = operator
        self.nodes = nodes
        self.edges = edges

    def run_lemma(self):

        # Get the edge to delete using the DFS
        edge_to_remove = Selector(self.edges)

        self.nodes, self.edges =  self._perform_lemma_op(edge_to_remove)



    def _perform_lemma_op(self, edge_to_remove):

        # Set-up to be able to run split_edges function
        graph = nx.Graph()
        self.edges = [(min(a, b), max(a, b)) for a, b in self.edges]
        graph.add_edges_from(self.edges)

        # Running the split_edges program
        # Returns an updated set of self.nodes and self.edges
        return split_edges(self.nodes, self.edges, edge_to_remove)





