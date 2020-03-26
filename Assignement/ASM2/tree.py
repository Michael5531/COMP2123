"""
Tree
-------

This is the tree file, it holds the main data structure that will be used for
testing. The tree contains a root node which then has children until the
leaves.
This is the main file for the interaction of tests.

Your task is to implement the methods for put and flatten.
"""

import node

class Tree:
    """
    Tree Class
    Holds nodes, where each node in the tree has children, unless it is a leaf,
    where it has 0 children.

    Each node in the tree is type <class Node> defined in `node.py`.

    - Init: Sets up the tree with the specified root node.
    - put(node, child): Adds the child node to the specified node in the tree.
    - flatten(node): flatten the node.
    - swap(subtree_a, subtree_b): Swap the position of the subtrees.
    """

    def __init__(self, root):
        """
        Initialises the tree with a root node.
        :param root: the root node.
        """
        self.root = root

    def put(self, node, child):
        """
        Inserts a node into the tree. Adds `child` to `node`.
        :param node: The node currently in the tree.
        :param child: The child to add to the tree.
        """
        node.add_child(child)

    def flatten(self, node):
        """
        Flatten the node given by removing the subtree rooted at this node.
        You must (a) flatten the subtree, (b) compute the sum of all nodes
        below and perform any updates
        to other nodes.

        :param node: The root of the subtree to flatten.

        Example

           A(5)
           / \
         B(3) C(6)
         /    |  \
        D(2) E(3) F(6)
        flatten(C)

           A(5)
           / \
         B(3) C(15)
         /
        D(2)
        """
        self.sum_calc(node)
        node.subtree_value = node.key # sum_calc
        node.children = []
        node.post_order()

    def sum_calc(self, node):
        if not node.is_external():
            count = 0
            for i in node.children:
                self.sum_calc(i) # is_external return true
                count += i.key
            node.key += count
        else:
            return node.key

    def swap(self, subtree_a, subtree_b):
        temp_a_parent = subtree_a.parent
        temp_b_parent = subtree_b.parent            # Set up temp parent
        temp_b_parent.children.remove(subtree_b) # Disconnect to parent
        temp_a_parent.children.remove(subtree_a)
        subtree_a.parent = temp_b_parent
        subtree_b.parent = temp_a_parent
        temp_b_parent.children.append(subtree_a)
        temp_a_parent.children.append(subtree_b)
        current_node = subtree_a
        while current_node.parent is not None:
            self.swap_calc(current_node)
            current_node = current_node.parent
        current_node = subtree_b
        while current_node.parent is not None:
            self.swap_calc(current_node)
            current_node = current_node.parent

    def swap_calc(self, node):
        temp = 0
        node.parent.subtree_value = node.parent.key  # re assign parent subtree_value to node.parent.key
        if node.subtree_value > node.parent.subtree_value:
            temp = node.subtree_value
        else:
            temp = node.parent.subtree_value
        for i in node.parent.children:
            if i.subtree_value > temp:
                temp = i.subtree_value
        node.parent.subtree_value = temp



        """
        Swap subtree A with subtree B
        :param subtree_a: The root node of subtree_a.
        :param subtree_b: The root node of subtree_b.

        Example:

            A
           / \
           B  C
         /   / \
        D   J   K

        SWAP(B, C)
            A
           / \
          C  B
         / |  \
        J  K   D
        """

