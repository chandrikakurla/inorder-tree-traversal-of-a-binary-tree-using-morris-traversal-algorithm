#class node to create nodes of binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#morris traversal algorithm
def MorrisTraversal(root):
    #initialising currentnode to root of binary tree
    currentnode=root
    while(currentnode is not None):
        #if left side is not present print current and assign current to current.right
        if currentnode.left is None:
            print(currentnode.data,end=" ")
            currentnode=currentnode.right
        #if left side is present
        else:
            #finding predecessor
            predec=currentnode.left
            while(predec.right is not None and predec.right!=currentnode):
                predec=predec.right
            #if right of predecessor is none then point right of predecessor to currentnode 
            #now we have track of currentnode so change currentnode to currentnode.left
            if(predec.right is None):
                predec.right=currentnode
                currentnode=currentnode.left
            #if right of predecessor points to currentnode means we have already visited left of currentnode
            #so print currentnode and update currentnode to currentnode.right
            #and make right of predecessor to again None so that we can get our original binary tree back
            else:
                predec.right=None
                print(currentnode.data,end=" ")
                currentnode=currentnode.right
#main programme
if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.right.right=Node(6)
    root.left.left=Node(4)
    root.left.right=Node(5)
    print("inorder traversal of binary tree using morris traversal:")
    MorrisTraversal(root)
