

# 节点类
class TreeNode(object):
    # def __init__(self, data=0, left=0, right=0):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 二叉树类
class BTree(object):
    def __init__(self, root = None):
        self.root = root

    def previous_order(self, tree_node):  # 前序
        if tree_node is None:
            return
        print(tree_node.data, end="   ")
        self.previous_order(tree_node.left)
        self.previous_order(tree_node.right)

    def in_order(self, tree_node):  # 中序
        if tree_node is None:
            return
        self.in_order(tree_node.left)
        print(tree_node.data, end="   ")
        self.in_order(tree_node.right)

    def post_order(self, tree_node):  # 后序
        if tree_node is None:
            return
        self.post_order(tree_node.left)
        self.post_order(tree_node.right)
        print(tree_node.data, end="   ")


"""
二叉树见二叉树.png
"""

if __name__ == '__main__':
    # 从叶子向根创建二叉树
    ne = TreeNode("e")
    ng = TreeNode("g")
    nd = TreeNode(data="d", right=ne)
    nf = TreeNode(data="f", left=ng)
    nb = TreeNode(data="b", left=nd, right=nf)
    nc = TreeNode(data="c")
    na = TreeNode(data="a", left=nb, right=nc)
    btree = BTree(na)  # 创建二叉树
    print("前序：")
    btree.previous_order(btree.root)
    print()
    print("中序：")
    btree.in_order(btree.root)
    print()
    print("后序：")
    btree.post_order(btree.root)
    print()
