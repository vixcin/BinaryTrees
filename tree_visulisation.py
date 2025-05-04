import matplotlib.pyplot as plt
import networkx as nx
from binary_tree import BinaryTree, Node

def create_graph_from_tree(root):
    G = nx.Graph()
    pos = {}
    
    def _add_nodes(node, x=0, y=0, layer=1):
        if node:
            G.add_node(node.value)
            pos[node.value] = (x, y)
            
            if node.left:
                G.add_edge(node.value, node.left.value)
                _add_nodes(node.left, x-1/2**layer, y-1, layer+1)
            
            if node.right:
                G.add_edge(node.value, node.right.value)
                _add_nodes(node.right, x+1/2**layer, y-1, layer+1)
    
    _add_nodes(root)
    return G, pos

def visualize_tree(tree, traversal_type=None, traversal_result=None):
    plt.figure(figsize=(10, 8))
    G, pos = create_graph_from_tree(tree.root)
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1000, font_size=16, font_weight='bold')
    
    if traversal_type and traversal_result:
        plt.title(f"{traversal_type} Traversal: {' → '.join(map(str, traversal_result))}")
    else:
        plt.title("Binary Tree Visualization")
    
    plt.show()


def demonstrate_tree_traversals():
    # Sample tree
    tree = BinaryTree()
    # random
    values = [5, 3, 7, 2, 4, 6, 8, 9, 10,  11, 777]
    for value in values:
        tree.insert(value)
    
    # Visualize the tree structure
    visualize_tree(tree)
    
    # In-Order Traversal
    inorder = tree.inorder_traversal()
    visualize_tree(tree, "Inorder", inorder)
    
    # preorder = tree.preorder_traversal()
    # visualize_tree(tree, "Preorder", preorder)
    
    # postorder = tree.postorder_traversal()
    # visualize_tree(tree, "Postorder", postorder)

if __name__ == "__main__":
    demonstrate_tree_traversals()