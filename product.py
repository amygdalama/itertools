import itertools
import pprint


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return str(self.data)

    def add_child(self, node):
        self.children.append(node)


class ProductTree(object):
    def __init__(self):
        self.root = Node("root")
        self.leaves = [self.root]

    def add_children(self, l):
        """Add children to all 'end' leaves."""
        new_leaves = []
        for leaf in self.leaves:
            for data in l:
                child = Node(data)
                leaf.add_child(child)
                new_leaves.append(child)
        self.leaves = new_leaves

    def create_from_lists(self, *args):
        for l in args:
            self.add_children(l)


def depth_first_traversal(node, branches=[]):
    print node
    for child in node.children:
        depth_first_traversal(child)


def product_by_tree(*args):
    t = ProductTree()
    t.create_from_lists(*args)
    return depth_first_traversal(t.root)


def product(*args):
    result = [[]]
    for arg in args:
        result = [prev + [x] for prev in result for x in arg]
    for prod in result:
        yield tuple(prod)


if __name__ == '__main__':
    result = product(range(7), range(2), range(5))
    expected = itertools.product(range(7), range(2), range(5))
    for exp, res in zip(expected, result):
        assert exp == res
    product_by_tree(range(3), range(2))