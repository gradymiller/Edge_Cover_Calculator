# This file takes in nodes and edges and determines the structure of the graph.
# Then, it returns a packed list, separating path graphs from everything else
# TODO: Works good but could use some more testing

import networkx as nx

class Identifier:
    def __init__(self, nodes, edges):
        self.graph = nx.Graph()
        self.graph.add_edges_from(edges)
        self.nodes = nodes
        self.edges = edges
        self.components_list = []
        self.component_amount = 0
        self.degrees = dict(self.graph.degree()) # type: ignore

    # Splits the edges up into their respective parts
    def separate_components(self):
        components = list(nx.connected_components(self.graph))
        self.components_list = [list(component) for component in components]

    def count_parts(self):
        return len(self.components_list) > 1

    # Converts the vertices to edges, to be used in the check_type() method
    def vertex_to_edge(self, vertices):
        return [edge for edge in self.edges if edge[0] in vertices and edge[1] in vertices]

    # Subtracts the path graphs out of the components list so non-path graphs can be outputted as the_rest
    def making_the_rest(self, path_graphs):
        # Flatten path_graphs (since it may contain lists of vertices)
        flat_path_graphs = [vertex for sublist in path_graphs for vertex in sublist]
        return [vertex for vertex in self.nodes if vertex not in flat_path_graphs]

    # This is the main function of the class, only this one needs to be run
    # It returns two things: the first is a list of path graphs, the second is a list of everything else
    def check_type(self):
        path_graphs = []
        the_rest = []
        self.separate_components()
        # If there is 1 path graph, it just returns it
        if not self.count_parts():
            path_graphs.append(self.components_list)  # Still keeping the structure for single component case
            return path_graphs, the_rest

        # This loop iterates over each component (each separate piece of the graph)
        for component in self.components_list:
            ones = 0
            degree_list = {}
            # This list iterates over every vertex and grabs the corresponding degree value for it
            for vertex in component:
                if vertex in self.degrees:
                    degree_list[vertex] = self.degrees[vertex]
            # This loop aids in checking for path graphs by getting the edges with a degree of 1
            for key, value in degree_list.items():
                if value == 1:
                    ones += 1  # Count how many items have degree of 1
                elif value != 2:
                    break  # If any degree is not 1 or 2, return False
            # Checks if it's a path graph based on previous data
            if ones == 2 and len(degree_list) - ones == list(degree_list.values()).count(2):
                path_graphs.append(component)  # Each component is appended as a separate list

        # Only call making_the_rest after checking that there are path graphs
        if path_graphs:
            # Convert the path graphs and the remaining vertices to edges for ease of use
            the_rest = self.making_the_rest(path_graphs)
            path_graph_edges = [self.vertex_to_edge(component) for component in path_graphs]
            other_edges = self.vertex_to_edge(the_rest)
        else:
            path_graph_edges = []
            other_edges = []

        return path_graph_edges, other_edges


# Testing...
test_nodes = [1, 3, 5, 6, 7, 8, 13, 14, 16]
test_edges = [(6, 1), (7, 3), (1, 3), (8, 5), (6, 13), (7, 14), (8, 16)]
test = Identifier(test_nodes, test_edges)
print(test.check_type())
























