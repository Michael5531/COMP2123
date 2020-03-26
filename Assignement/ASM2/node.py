"""
Tree Node
----------

This node represents an item in the tree. Each node contains its key as well as
the value of the subtree rooted at this node. It supports operations to add
children, as well as check if this is a leaf or not.
"""


class Node:
    """
    Node Class
    - Init: Sets the basic information such as the key, children, and value of
    subtree.
    - add_child(child_node): Adds the child node to the list of children.
    - is_external(): Checks if the node is a leaf.
    - children(): returns the list of children.
    """

    def __init__(self, key, parent=None):
        """
        The initialisation of the node sets the key and instantiates the
        children (as empty).
        :param key: The value of the node.
        :param parent: The parent of the node.
        """
        self.key = key
        self.parent = parent
        self.subtree_value = key
        self.children = []

    def add_child(self, child_node):
        """
        Adds `child_node` as a child of this node. Adds to the list of children
        and performs required calculations.
        :param child_node: The child node to add (class Node)
        """
        value = self.key
        self.children.append(child_node)
        child_node.parent = self
        if child_node.subtree_value > self.subtree_value:
            self.subtree_value = child_node.subtree_value
            self.post_order()

    def post_order(self):
        current_node = self
        while current_node.parent != None:
            if current_node.subtree_value > current_node.parent.subtree_value:
                current_node.parent.subtree_value = current_node.subtree_value # UPDATE to parent node to the current node
                current_node = current_node.parent
            else:
                break

    def is_external(self):
        """
        Checks if the node is a leaf node in the tree.
        :return: Boolean, True if leaf, False otherwise.
        """
        # Return boolean value
        return len(self.children) == 0

    def get_children(self):
        """
        Returns the children of the current node.
        :return: List of children.
        """

        # Can also access this using "node.children", but putting
        # this here for ease of use and standard usage things in
        # other languages people might be used to.
        return self.children




