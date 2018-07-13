
class Tree(object):
    def __init__(self):
        self.node_list = []

    def startTree(self):
        root = self.insertNode(1, None, None, True)
        root.left = self.insertNode(2)
        root.right = self.insertNode(3)
        root.left.left = self.insertNode(4)
        root.left.right = self.insertNode(5)
        root.right.left = self.insertNode(6)
        root.right.right = self.insertNode(7)

    def insertNode(self, value, left = None, right = None, root_node = False):
        t = TreeNode(value, left, right, root_node)
        self.node_list.append(t)
        return t

    def inorder_traverse(self):

        root = 0
        for i in self.node_list:
            if i.getRootNodeStatus():
                print i.getValue()

                root = i

        print root.left.getValue()
        print root.left.left.getValue()
        print root.left.right.getValue()
        print root.right.getValue()
        print root.right.left.getValue()
        print root.right.right.getValue()

    def mirror_view_inorder(self):
        root = 0
        for i in self.node_list:
            if i.getRootNodeStatus():
                print i.getValue()

                root = i

        print root.right.getValue()
        print root.right.right.getValue()
        print root.right.left.getValue()
        print root.left.getValue()
        print root.left.right.getValue()
        print root.left.left.getValue()
            

                
               



class TreeNode(object):
    def __init__(self, value, left, right, root_node):
        self.value = value
        self.left = left
        self.right = right
        self.root_node = root_node

    def getValue(self):
        return self.value

    def getLeftNode(self):
        return self.left

    def getRightNode(self):
        return self.right

    def getRootNodeStatus(self):
        return self.root_node


    #             t1
    #     t2                t3
    # t4      t5     | t6         t7

def main():

    tree = Tree()
    tree.startTree()

    tree.inorder_traverse()
    print "mirror_view_inorder"
    tree.mirror_view_inorder()


main()

