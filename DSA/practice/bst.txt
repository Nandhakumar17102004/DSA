import math
class BinarySearchTree:
    """
    This defines the node class. The children can be individually declared or stored
    in a list. We are adding a pos value which stores the nodes
    position. root nodes pos value is 1
    """
    class node:
        def __init__(self):
            self.element = 0
            self.left= None
            self.right= None
            self.pos = -1
            self.parent = None
    """
        This initializes the binary search tree. ht is the height of the tree, sz is the
        number of nodes. You may define this appropriately.
    """
    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0

    """
        This method implements the functionality of finding an element in the tree. The function
        findElement(e) finds the node in the current tree, whose element is e. Depending on the
        value of e and in relation to the current element visited, the algorithm visits the left
        or the right child till the element is found, or an external node is visited. Your
        algorithm can be iterative or recursive

        Output: Returns the pointer to the node
    """
                 
    def findElement(self,e,curnode):
        #@start-editable@
        #pass
        if curnode==None:
            return
        elif e>curnode.element:
            return self.findElement(e,curnode.right)
        elif e<curnode.element:
            return self.findElement(e,curnode.left)
        else:
            return curnode

        #@end-editable@
            
    """
        This method implements insertion of an element into the binary search tree. Using the
        findElement(e) method find the position to insert, and insert a node with element e,
        as left or right child accordingly. Make sure that you update the value of pos attribute.
        curnode.leftchild.pos = curnode.pos * 2
        curnode.rightchild.pos = curnode.pos * 2 + 1    
    """
    def insertElement(self,curnode,e):
    #@start-editable@
        if curnode is None:
            x=self.node()
            x.element=e
            if self.sz==0:
                x.pos=1
                self.root=x
                self.sz+=1
            return x
        else:
            if e<curnode.element:
                curnode.left = self.insertElement(curnode.left, e)
                curnode.left.pos=curnode.pos*2
                curnode.leftchildpos=curnode.pos*2
                self.sz+=1
            else:
                curnode.right = self.insertElement(curnode.right, e)
                curnode.right.pos=curnode.pos*2+1
                curnode.rightchildpos=curnode.pos*2+1
                self.sz+=1
        return curnode

    #@end-editable@
    """
        This method inorderTraverse(self,v) performs an inorder traversal of the BST, starting
        from node v which is initially the root and prints the elements of the nodes as they
        are visited. Remember the inorder traversal first visits the left child, followed by
        the parent, followed by the right child. This could be used to print the tree.
    """
    def inorder_traversal(self,root):
    #@start-editable@
        if root:
            self.inorder_traversal(root.left)
            print(root.element)
            self.inorder_traversal(root.right)

    #@end-editable@

    """
        Given a node v this will return the next element that should be visited after v in the
        inorder traversal. You can define this recursively
    """
    def returnNextInorder(self,v):
    #@start-editable@
        pass
    #@end-editable@
    """
        This method deleteElement(self, e), removes the node with element e from the tree T.
        There are three cases:
            1. Deleting a leaf or external node:Just remove the node
            2. Deleting a node with one child: Remove the node and replace it with its child
            3. Deleting a node with two children: Instead of deleting the node replace with
                a) its inorder successor node or b)Inorder predecessor node
    """

    def deleteElement(self, root, key):
        # Base case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
        if key < root.element:
            root.left = self.deleteElement(root.left, key)
        # If the key to be deleted is greater than the root's key, then it lies in the right subtree
        elif key > root.element:
            root.right = self.deleteElement(root.right, key)
        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.element = self.minValue(root.right)

            # Delete the inorder successor
            root.right = self.deleteElement(root.right, root.element)

        return root

    def minValue(self, root):
        minv = root.element
        while root.left:
            minv = root.left.element
            root = root.left
        return minv

        
    """
        There are other support methods which maybe useful for implementing your functionalities.
        These include
            1. isExternal(self,v): which returns true if the node v is external
    """
    def isExternal(self,curnode):
        if (curnode.left == None and curnode.right== None):
            return True
        else:
            return False
        
    def external_nodes(self,curnode):
        if curnode:
            if self.isExternal(curnode):
                print(curnode.element,end=' ')
            self.external_nodes(curnode.left)
            self.external_nodes(curnode.right)
            
    def descendants(self,curnode):
        if curnode:
            if curnode.left:
                print(curnode.left.element,end=' ')
                self.descendants(curnode.left)
            if curnode.right:
                print(curnode.right.element,end=' ')
                self.descendants(curnode.right)
                
    def ancestors(self,root,e):
        ancestors = []
        self.findAncestors(root, e, ancestors)
        for i in ancestors:
            print(i.element,end=' ')
        print()
        return

    def findAncestors(self,node, target, ancestors):
        if node is None:
            return False

        if node.element == target:
            return True

        if self.findAncestors(node.left, target, ancestors) or self.findAncestors(node.right, target, ancestors):
            ancestors.append(node)
            return True
        return False

    def path(self,root,e):
        if e==self.findElement(e,root).element:
            path = [self.findElement(e,root)]
            self.findAncestors(root, e, path)
            path=path[::-1]
            for i in path:
                print(i.element,end=' ')
            print()
        else:
            print("Unknown element")

    def sibling(self,root,e):
        ancestors = []
        self.findAncestors(root, e, ancestors)
        parent=ancestors[0]
        if parent.left.element==e:
            if parent.right!=None:
                print(parent.right.element)
                return
            print("No Sibling")
        else:
            if parent.left!=None:
                print(parent.left.element)
                return
            print("No Sibling")

            
    def getChildren(self, ele):
    #@start-editable@
        key=tree.findElement(ele,self.root)
        if(key.element != ele):
            print("Element Not Found")
            return
        else:
            if self.isExternal(key):
                print("No Children")
                return
            if key.left:
                print("Left Child:",key.left.element)
            if key.right:
                print("Right Child:",key.right.element)
    #@end-editable@
    
    def preorder_traversal(self,root):
    #@start-editable@
        if root:
            print(root.element)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
    #@end-editable@
        
    def postorder_traversal(self,root):
    #@start-editable@
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.element)
    #@end-editable@

    def findDepthIter(self,v):
    #@start-editable@
	    pass
	#@end-editable@
    
    def findDepth(self,ele):
        curnode = self.findElement(ele,self.root)
        if(curnode.element != ele):
            print("No such Element")
            return
        else:
            return self.findDepthIter(curnode)

    def findHeight(self,ele):
    #@start-editable@
        pass
	#@end-editable@
	
def main():
    tree = BinarySearchTree()
    #print("Array Size:")
    #arraySize = int(input())
    #print("Array Elements:")
    #arr = list(map(int, input().split()))
    arraySize = 7
    arr=[10,5,8,15,13,7,6]
    for i in range(arraySize):
        tree.insertElement(tree.root,arr[i])
    """tree.insertElement(50)
    tree.insertElement(20)
    tree.insertElement(70)
    tree.insertElement(1)
    tree.insertElement(10)
    tree.insertElement(90)
    tree.insertElement(15)
    tree.insertElement(30)
    tree.insertElement(60)
    tree.insertElement(61)
    tree.insertElement(62)
    tree.insertElement(65)
    tree.insertElement(8)
    tree.insertElement(100)"""
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="I"):
            tree.inorder_traversal(tree.root)
            print()
        elif(operation[0]=="P"):
            tree.preorderTraverse(tree.root)
            print()
        elif(operation[0]=="Post"):
            tree.postorderTraverse(tree.root)
            print()
        elif(operation[0]=="D"):
            tree.deleteElement(tree.root,int(operation[1]))
        elif(operation[0]=="Externalnodes"):
            tree.external_nodes(tree.root)
            print()
        elif(operation[0]=="Descendant"):
            tree.descendants(tree.root)
            print()
        elif(operation[0]=="Ancestor"):
            tree.ancestors(tree.root,int(operation[1]))
        elif(operation[0]=="Path"):
            tree.path(tree.root,int(operation[1]))
        elif(operation[0]=="Sibling"):
            tree.sibling(tree.root,int(operation[1]))
        elif(operation[0]=="H"):
            print(tree.findHeight(int(operation[1])))
        elif(operation[0]=="Depth"):
            print(tree.findDepth(int(operation[1])))
        elif(operation[0]=='Find'):
            key = tree.findElement(int(operation[1]), tree.root)
            if(key.element == int(operation[1])):
                print("Element Found at", key.pos)
            else:
                print("Element not Found")
        elif(operation[0]=="GetC"):
            childs = tree.getChildren(int(operation[1]))
            print(childs)
        inputs-=1

if __name__ == '__main__':
    main()
