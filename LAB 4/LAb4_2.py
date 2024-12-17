class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []  # List to hold children nodes

    def add_child(self, child_node):
        self.children.append(child_node)

def iddfs(root, goal):
    for i in range(0,100000):
        res=dls(root,goal,i)
        if res:
            print("Found")
            return
    print("Not found")

def dls(root,goal,depth):
    if depth==0:
        if root.value==goal:
            return True
        return False
    for child in root.children:
        if dls(child,goal,depth-1):
            return True
    return False

root=TreeNode("Y")
node1=TreeNode("P")
node2=TreeNode("X")
node3=TreeNode("R")
node4=TreeNode("S")
node5=TreeNode("F")
node6=TreeNode("H")
node7=TreeNode("B")
node8=TreeNode("C")
node9=TreeNode("S")

root.add_child(node1)
root.add_child(node2)

node1.add_child(node3)
node1.add_child(node4)

node2.add_child(node5)
node2.add_child(node6)

node3.add_child(node7)
node3.add_child(node8)

node4.add_child(node9)

iddfs(root, "F")
iddfs(root, "A")
