import networkx as nx
from collections import defaultdict

class Graph:
    def __init__(self, edges):
        self.time = None
        self.graph = defaultdict(list)
        self.edges = edges
        self.V = self._get_vertex_count(edges)
        self.add_edges(edges)

    @staticmethod
    def _get_vertex_count(edges):
        return max(max(u, v) for u, v in edges) + 1

    def add_edges(self, edges):
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def bridge_util(self, u, visited, parent, discovery_time, low, bridges):
        visited[u] = True
        discovery_time[u] = self.time
        low[u] = self.time
        self.time += 1 # type: ignore

        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.bridge_util(v, visited, parent, discovery_time, low, bridges)
                low[u] = min(low[u], low[v])

                if low[v] > discovery_time[u]:
                    bridges.append((u, v))

            elif v != parent[u]:
                low[u] = min(low[u], discovery_time[v])

    def find_bridges(self):
        visited = [False] * self.V
        discovery_time = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        bridges = []
        self.time = 0

        for i in range(self.V):
            if not visited[i]:
                self.bridge_util(i, visited, parent, discovery_time, low, bridges)

        return bridges

    def dfs_cycle(self, u, visited, parent, cycle_edges, vertex_in_cycle):
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                if self.dfs_cycle(v, visited, u, cycle_edges, vertex_in_cycle):
                    return True
            elif v != parent:
                # We've found a cycle edge
                cycle_edges.add((min(u, v), max(u, v)))  # Add cycle edge
                vertex_in_cycle.add(u)
                vertex_in_cycle.add(v)
                return True
        return False

    def find_cycle_and_vertices(self):
        visited = [False] * self.V
        cycle_edges = set()
        vertex_in_cycle = set()

        for i in range(self.V):
            if not visited[i]:
                if self.dfs_cycle(i, visited, -1, cycle_edges, vertex_in_cycle):
                    break
        return cycle_edges, vertex_in_cycle

    def find_highest_combined_degree_edge(self):
        G = nx.Graph()
        G.add_edges_from(self.edges)

        # Get the degrees of all nodes
        degrees = dict(G.degree())  # type: ignore # Create a dictionary {node: degree}

        # Initialize variables to track the highest combined degree and the corresponding edge
        max_combined_degree = -1
        best_edge = None

        # Loop through each edge to find the edge with the highest combined degree
        for u, v in self.edges:
            combined_degree = degrees[u] + degrees[v]  # Sum of degrees of both vertices of the edge

            # Update the best edge if this one has a higher combined degree
            if combined_degree > max_combined_degree: # type: ignore
                max_combined_degree = combined_degree
                best_edge = (u, v)

        return best_edge

    def find_best_edge_to_remove(self):
        G = nx.Graph()
        G.add_edges_from(self.edges)
        degrees = dict(G.degree()) # type: ignore
        ones = 0
        for key, value in degrees.items():
            if value == 1:
                ones += 1  # Count how many items have value 1
            elif value != 2:
                break  # If any value is not 1 or 2, return False

        if ones == 2 and len(degrees) - ones == list(degrees.values()).count(2): # type: ignore
            return None
        else:
            bridges = self.find_bridges()
            if bridges:
                bridges.reverse()
                return bridges[0], 'B'

            # Find the first cycle and the vertices that are part of that cycle
            cycle_edges, vertex_in_cycle = self.find_cycle_and_vertices()

            if not cycle_edges and not bridges:  # If no cycles and no bridges
                return None

            # Remove the edge with the highest combined degree in the cycle
            best_edge = self.find_highest_combined_degree_edge()
            return best_edge, 'C'

edges = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 5)]
graph = Graph(edges)
best_edge_to_remove = graph.find_best_edge_to_remove()
print(best_edge_to_remove)

# Cycle: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
# Path: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
# Tadpole: [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4)]
# Double Rocket: [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 0), (1, 7), (3, 5)]
# Kayak: [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3)]