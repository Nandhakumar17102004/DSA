import math
class PropertyListing:
    
    class property:
        def __init__(self):
            self.price = 0
            self.listingid=None
            self.address=None
            self.sqfootage=None
            self.nbedroom=None
            self.nbathroom=None
            self.listingagent=None
            self.left= None
            self.right= None
            self.pos = -1
    
    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0

    """
        This method implements the functionality of finding an price in the tree. The function
        findprice(e) 
        Output: Returns the pointer to the node
    """
                 
    def findProperty(self,e,curnode):
        #@start-editable@
        #pass
        if curnode==None:
            return
        elif e>curnode.price:
            return self.findProperty(e,curnode.right)
        elif e<curnode.price:
            return self.findProperty(e,curnode.left)
        else:
            return curnode

        #@end-editable@
            
    """
        This method implements insertion of an property into the binary search tree.
    """
    def insertproperty(self,curnode,e,id,ad,sqft,nb1,nb2,la):
        if curnode is None:
            x=self.property()
            x.price=e
            x.listingid=id
            x.address=ad
            x.sqfootage=sqft
            x.nbedroom=nb1
            x.nbathroom=nb2
            x.listingagent=la
            if self.sz==0:
                x.pos=1
                self.root=x
                self.sz+=1
            return x
        else:
            if e<curnode.price:
                curnode.left = self.insertproperty(curnode.left, e,id,ad,sqft,nb1,nb2,la)
                curnode.left.pos=curnode.pos*2
                curnode.leftchildpos=curnode.pos*2
                self.sz+=1
            else:
                curnode.right = self.insertproperty(curnode.right, e,id,ad,sqft,nb1,nb2,la)
                curnode.right.pos=curnode.pos*2+1
                curnode.rightchildpos=curnode.pos*2+1
                self.sz+=1
        return curnode

    
    """
        This method deleteproperty(self, e), removes the node with price e from the tree T.
        There are three cases:
            1. Deleting a leaf or external node:Just remove the node
            2. Deleting a node with one child: Remove the node and replace it with its child
            3. Deleting a node with two children: Instead of deleting the node replace with
                a) its inorder successor node or b)Inorder predecessor node
    """

    def deleteproperty(self, root, key):
        if root is None:
            return root

        if key < root.price:
            root.left = self.deleteproperty(root.left, key)
        elif key > root.price:
            root.right = self.deleteproperty(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.price = self.minValue(root.right)
            # Delete the inorder successor
            root.right = self.deleteproperty(root.right, root.price)

        return root

    def minValue(self, root):
        minv = root.price
        while root.left:
            minv = root.left.price
            root = root.left
        return minv

    def updateproperty(self, root, old_price, new_price):
        x=self.findProperty(old_price,root)
        self.deleteproperty(self.root,old_price)
        x.price=new_price
        self.insertproperty(self.root,x.price,x.listingid,x.address,x.sqfootage,x.nbedroom,x.nbathroom,x.listingagent)
    
    def isExternal(self,curnode):
        if (curnode.left == None and curnode.right== None):
            return True
        else:
            return False
        
    def search_range(self,root,propertylist,minimum,maximum):
        if root:
            if minimum<=root.price<=maximum:
                propertylist.append(root)
            self.search_range(root.left,propertylist,minimum,maximum)
            self.search_range(root.right,propertylist,minimum,maximum)
        return propertylist
    
    def preorder_traversal(self,root):
        if root:
            print(root.price)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
        
def main():
    # Create an instance of PropertyListing
    property_listing = PropertyListing()

    # Add some properties
    property_listing.root = property_listing.insertproperty(property_listing.root, 100000, 1, "123 Main St", 1500, 3, 2, "John Doe")
    property_listing.root = property_listing.insertproperty(property_listing.root, 150000, 2, "456 Elm St", 2000, 4, 3, "Jane Smith")
    property_listing.root = property_listing.insertproperty(property_listing.root, 200000, 3, "789 Oak St", 1800, 3, 2, "Alice Johnson")
    property_listing.root = property_listing.insertproperty(property_listing.root, 250000, 4, "321 Pine St", 2200, 4, 3, "Bob Williams")

    # Search for properties within a price range
    minimum_price = 150000
    maximum_price = 250000
    properties_within_range = property_listing.search_range(property_listing.root, [], minimum_price, maximum_price)
    print("Properties within the price range of ${} to ${}:".format(minimum_price, maximum_price))
    for prop in properties_within_range:
        print("ID:", prop.listingid, "| Address:", prop.address, "| Price:", prop.price)

    # Update the price of a property
    old_price = 150000
    new_price = 180000
    property_listing.updateproperty(property_listing.root, old_price, new_price)
    print("\nAfter updating the price of property with ID", old_price, "to", new_price)
    property_listing.preorder_traversal(property_listing.root)

    # Delete a property
    property_to_delete = 200000
    property_listing.root = property_listing.deleteproperty(property_listing.root, property_to_delete)
    print("\nAfter deleting the property with ID", property_to_delete)
    property_listing.preorder_traversal(property_listing.root)

if __name__ == "__main__":
    main()
