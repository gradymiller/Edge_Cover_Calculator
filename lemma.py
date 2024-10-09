# This file applies the cutting-open lemma on a graph
# It inputs the nodes, edges, and an edge to delete
# Then it splits the edges and adds the extra edge like the lemma requires
# NOTE: This function does not return anything, it just updates the parameters
import networkx as nx
# TODO: Test with multiple graphs, it works for the one below
# This code for is for the case with e
# The nodes and edges are there just for testing

graph = nx.Graph()
nodes = [1, 2, 3, 4, 5]
edges = [(1, 2), (2, 3), (3, 1), (2, 4), (4, 5)]
# This below reorders the edges so that the smallest number is first, making it easier to work with
edges = [(min(a, b), max(a, b)) for a, b in edges]
graph.add_edges_from(edges)
degrees = graph.degree()  # type: ignore
deleted_edge = (2, 4)
num1 = deleted_edge[0]
num2 = deleted_edge[1]

# The if-else statement only does the splitting if the edge is connected to other edges
# The vertex is deleted if the degree is 1, meaning only 1 edge connected to it


def split_edges(nodes, edges, deleted_edge):
    edges.remove(deleted_edge)
    highest_num_vertex = 0
    for vertex in deleted_edge:
        if degrees[vertex] > 1:
            # Gets edges that are touching the vertex in deleted_edge
            edges_to_split = [i for i in edges if vertex in i]
            edges_to_split_copy = edges_to_split[:]
            # This orders the numbers in each pair so that num1 is first
            edges_to_split = [(vertex, a if a != vertex else b) if vertex in (
                a, b) else (a, b) for a, b in edges_to_split]
            #  This is used to check the highest numbered node so it knows what to make the new edges with
            i = nodes[-1]
            # Remembers the first new node, for adding the extended edges from using the lemma
            # place_holder1 = i + 1
            # replaces all the edges_to_split with new edges
            # leaving one the first pair with num1 so that vertex isn't completely gone
            edge_list_temp = []
            for num in range(len(edges_to_split)):
                i += 1
                edges_to_split[num] = (i, edges_to_split[num][1])
                nodes.append(i)
                edge_list_temp.append(i)
                highest_num_vertex = i

            # print(edges)
            # Updates the edges list with the new set
            for j in range(len(edges_to_split_copy)):
                index = edges.index(edges_to_split_copy[j])
                edges[index] = edges_to_split[j]

            # Making new edges
            new_list = []
            for item in edge_list_temp:
                new_list.append((item, item + highest_num_vertex))
            # Adding the new edges onto the graph after everything is split
            edges += new_list

            # Testing...
            # print(edge_list_temp)
            # print(new_list)
            # print(edges_to_split)

        else:
            nodes.remove(num1)


# print(nodes)
# print(edges)
split_edges(nodes, edges, deleted_edge)
# print(nodes)
print(edges)
