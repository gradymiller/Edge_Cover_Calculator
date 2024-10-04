import matplotlib.pyplot as plt
import networkx as nx
# This class does everything involving the input page.
# The usable methods are show() and get_data()
# Use show() to run everything and make a plot
# Use get_data() to return the nodes and edges
# TODO: Add a delete node option
# TODO: Fix the edge lines so that they don't go over the nodes
class InputPage:
    def __init__(self):
        # Using NetworkX to initialize a graph
        self.graph = nx.Graph()
        self.pos = {}
        # This is used to make a list of nodes
        self.vertex_count = 0
        self.selected_vertices = []
        # This is the list that holds the edges that are outputted for usage
        self.edges = []
        self.edge_selection_mode = False
        # Set up for a nice-looking GUI
        self.fig, self.ax = plt.subplots()

    # Adds the node to the graph and plots it
    def _add_vertex(self, event):
        # This increment is for when a list of nodes is needed
        self.vertex_count += 1
        vertex = self.vertex_count
        self.graph.add_node(vertex)
        self.pos[vertex] = (event.xdata, event.ydata)
        # These are the plotting lines, this is where to change the formatting of the nodes too
        plt.plot(event.xdata, event.ydata, 'o', markersize=12, color='red')
        plt.text(event.xdata, event.ydata, str(vertex), fontsize=12, ha='center', va='center')
        plt.draw()

    # Adds edges to the nx.Graph()
    def _connect_vertices(self, event):
        x, y = event.xdata, event.ydata
        for vertex, position in self.pos.items():
            if (x - position[0]) ** 2 + (y - position[1]) ** 2 < 0.01:
                self.selected_vertices.append(vertex)
                break
        # Does the matplotlib plotting part of it
        # Change edge formatting here
        if len(self.selected_vertices) == 2:
            v1, v2 = self.selected_vertices
            self.graph.add_edge(v1, v2)
            self.edges.append((v1, v2))
            x_values = [self.pos[v1][0], self.pos[v2][0]]
            y_values = [self.pos[v1][1], self.pos[v2][1]]
            plt.plot(x_values, y_values, color='black')
            self.selected_vertices = []
            plt.draw()

    def _delete_edge(self, edge):
        if self.graph.has_edge(*edge):
            self.graph.remove_edge(*edge)
            self.edges.remove(edge)
            self._update_edges()

    # There is probably an easier way to do this that just saves all the previous settings
    # I just reset the whole graph and redid the formatting so that it was the same
    # IMPORTANT: If formatting ever needs to be changed, this needs to be updated too
    def _update_edges(self):
        for line in self.ax.get_lines():
            line.remove()
        for v1, v2 in self.edges:
            x_values = [self.pos[v1][0], self.pos[v2][0]]
            y_values = [self.pos[v1][1], self.pos[v2][1]]
            self.ax.plot(x_values, y_values, color='black')
        for vertex, position in self.pos.items():
            self.ax.plot(position[0], position[1], 'o', markersize=12, color='red')
        nx.draw_networkx_labels(self.graph, self.pos, font_size=12, font_color='black', ax=self.ax)
        plt.draw()

    # I set this functionality almost identically to the documentation because I didn't understand it fully
    # It works without problems, so I didn't try to figure it out too much
    def _onclick(self, event):
        if event.dblclick:
            self._add_vertex(event)
        else:
            if not self.edge_selection_mode:
                self._connect_vertices(event)
            else:
                self._select_edge_to_delete(event)

    # Had to get some ChatGPT help on this part
    # It selects the edge if is within 0.02
    def _select_edge_to_delete(self, event):
        x, y = event.xdata, event.ydata
        for edge in self.edges:
            v1, v2 = edge
            x1, y1 = self.pos[v1]
            x2, y2 = self.pos[v2]
            dist = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
            if dist < 0.02:
                self._delete_edge(edge)
                break
    # TODO: Someday change this so it outputs the print() statements on the plot instead of the terminal
    # Switches edge_selection_mode between True and False
    def _toggle_edge_selection(self, event=None):
        self.edge_selection_mode = not self.edge_selection_mode
        if self.edge_selection_mode:
            print("Edge deletion mode activated.")
        else:
            print("Edge deletion mode deactivated.")

    # This is the main method of the class. It sets the plot up and connects the events
    def show(self):
        # This code sets up the plot and header
        self.ax.set_title("Double Click: Vertex | Single Click: Edge | \'e\': Toggle Deletion Mode\n--- Click inside of the grid --- ")
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_facecolor('white')
        # Looks for clicks and double-clicks and runs the method needed
        self.fig.canvas.mpl_connect('button_press_event', self._onclick)
        self.fig.canvas.mpl_connect('key_press_event', self._toggle_edge_selection)
        plt.show()

    # Second method to use for this class
    # Returns nodes and edges as long as show() has been run previously
    def get_data(self):
        nodes = list(range(1, self.vertex_count + 1))
        edges = self.edges
        return nodes, edges


# Testing...
plot = InputPage()
plot.show()
nodes, edges = plot.get_data()
print(nodes, edges)