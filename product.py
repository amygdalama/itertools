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


def depth_first_traversal(node, path=[]):
    
    for child in node.children:
        if not node.data == "root":
            path.append(node)
        depth_first_traversal(child, path)

    if len(path) > 0:
        line = path[:]
        line.append(node)
        print tuple(line)
        path.pop(0)


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
    result = product(xrange(0, 3), xrange(4, 6))
    expected = itertools.product(xrange(0, 3), xrange(4, 6))
    print "itertools.product:"
    for exp, res in itertools.izip(expected, result):
        print res
        assert exp == res

    print "product_by_tree:"
    pbt = product_by_tree(xrange(0,3), xrange(4,6))
