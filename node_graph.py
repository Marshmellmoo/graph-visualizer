
class Node:
    def __init__(self, label):
        self.label = label
        self._neighbors = []
    
    def has_edge(self, node):
        return node in self._neighbors
    
    def add_neighbor(self, node):
        self._neighbors.append(node)

class NodeGraph:
    
    def __init__(self, graph_name: str):
        self.graph_name = graph_name
        self._all_nodes = {}
    
    def get_node(self, label):
        
        if label not in self._all_nodes:
            self.add_node(label)

    def add_node(self, label):
        
        if label in self._all_nodes:
            raise ValueError("Node " + label + " already in graph.")
        
        node = Node(label)
        self._all_nodes[label] = node
    
    def connect(self, label1, label2):
        
        node1 = self.get_node(label1)
        node2 = self.get_node(label2)

        if not node1.has_edge(node2):
            node1.add_neighbor(node2)
        
        if not node2.has_edge(node1):
            node2.add_neighbor(node1)

    def get_neighbors(self, label):
        
        node = self.get_node()
        neighbors = set()

        for n in node._next_nodes:
            neighbors.add(n.label)
        
        return neighbors

    def get_all_nodes(self):
        
        nodes = set()
        for n in self._all_nodes:
            nodes.add(n)
        
        return nodes
