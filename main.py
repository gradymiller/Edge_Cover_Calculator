# Instead of finding the formula, find edges covers of sequence, find simplest combo of fibonacci formula that satisfies all #s in sequence
# TODO: alter input so that it knows where to add edges in the graph(X_n, where to increase n)
# TODO: Calculate the sequence a ton of times out
# TODO: Find a simple function using fibonacci_n that satisfies the sequence
# TODO: Output the general parent function for the graph
# TODO: Make each part into usable function
# TODO: Graphviz
# Potential Idea: Prompt for function_0 and where to expand at, program cutting open lemma for the basic function

from matplotlib.pyplot import show
import networkx as nx
from itertools import chain, combinations

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, int(n) + 1):
            a, b = b, a + b
        return b

def edge_cover_calc(edges):
    # Generating graph view
    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True, font_weight='bold')
    #Calculating edge covers
    def powerset(e):
        return chain.from_iterable(combinations(e, r) for r in range(len(e)+1))
    num_edge_covers = 0
    for eset in powerset(G.edges):
        if nx.is_edge_cover(G, eset):
            num_edge_covers += 1
    num_vertices = G.number_of_nodes()
    num_edges = G.number_of_edges()
    return num_vertices, num_edges, num_edge_covers




def main():
    # edges = [(0, 1), (7, 1), (8, 0), (4, 5), (5, 6), (9, 6), (7, 10), (8, 11), (9, 12), (12, 4)]
    edges = [(6, 1), (7, 3), (1, 3), (8, 5), (6, 13), (7, 14), (8, 16)]
    edge_cover_calc(edges)
    show()
main()
