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

    def __repr__(self):
        pass

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


def depth_first_traversal(node):
    queue = [[node]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node.children:
            for child in node.children:
                new_path = path[:]
                new_path.append(child)
                queue.append(new_path)
        else:
            yield tuple(path[1:])


def product_by_tree(*args):
    t = ProductTree()
    t.create_from_lists(*args)
    paths = depth_first_traversal(t.root)
    return paths


def other_product(*args):
    args = list(args)
    l = args.pop(0)
    result = [[elem] for elem in l]
    while args:
        l = args.pop(0)
        new_result = []
        for res in result:
            for elem in l:
                new_result.append(res + [elem])
        result = new_result
    return [tuple(r) for r in result]


def product(*args):
    result = [[]]
    for arg in args:
        result = [prev + [x] for prev in result for x in arg]
    for prod in result:
        yield tuple(prod)


if __name__ == '__main__':
    expected = itertools.product(xrange(0, 3), xrange(4, 6))
    doc_prod = product(xrange(0, 3), xrange(4, 6))
    tree_prod = product_by_tree(xrange(0, 3), xrange(4, 6))
    other_prod = other_product(xrange(0, 3), xrange(4, 6))
    for results in itertools.izip(expected, doc_prod, tree_prod, other_prod):
        assert all(repr(r) == repr(results[0]) for r in results)