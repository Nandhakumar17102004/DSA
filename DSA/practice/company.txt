'''
SCENARIO-2
class Node:
    def __init__(self,name,s,d):
        self.name=name
        self.directory=d
        self.left=None
        self.right=None
        self.size=s
class FileManager:
    def __init__(self):
        self.root=None
    def listfile(self,node):
        if node:
            self.listfile(node.left)
            print(node.name)
            self.listfile(node.right)
        else:
            return
    def search(self,node,file):
        if node:
            if node.name==file:
                print(node.name,"found")
                return node.name
            found=self.search(node.left,file)
            if found:
                return found
            found=self.search(node.right,file)
            if found:
                return found
    def calcsize(self,node):
        if node:
            left=self.calcsize(node.left)
            right=self.calcsize(node.right)
            if node.directory:
                return left+right+node.size
            else:
                return node.size
        else:
            return 0
root=Node("Root", 0, True)
root.left=Node("Downloads", 300, True)
root.right=Node("whatsapp", 100, True)
root.left.left=Node("dsa1.txt", 30, False)
root.left.right=Node("dsa2.txt", 20, False)
root.right.left=Node("W1.jpg", 50, False)
root.right.right=Node("M2.mp3", 15, False)

fs = FileManager()
fs.root = root

print("Listing all files and directories.....")
fs.listfile(fs.root)
print('\n')

print("Searching M2.mp3.....")
search_result = fs.search(fs.root, "M2.mp3")
if search_result:
    print("Sucess")
else:
    print("File not found.")
print('\n')

total_size = fs.calcsize(fs.root)
print("Total size of directory structure:", total_size)
'''

#####################################################################################################################

'''
SCENARIO-4
class Node:
    def __init__(self,name,eid,d,manager=None):
        self.eid=eid
        self.name=name
        self.designation=d
        self.child=[]
        self.report_to=manager
class Company:
    def __init__(self):
        self.employees={}
        
    def add_ceo(self,node):
        self.employees[node.eid]=node
        
    def add_employee(self,eid,name,d,r):
        node=Node(name,eid,d,r)
        rnode=self.employees[r]
        rnode.child.append(node)
        self.employees[eid]=node
        
    def resignation(self,eid):
        node=self.employees[eid]
        rnode=self.employees[node.report_to]
        rnode.child.remove(node)
        rnode.child.extend(node.child)
        del self.employees[node.eid]
        
    def delete_manager(self,eid):
        node=self.employees[eid]
        rnode=self.employees[node.report_to]
        rnode.child.remove(node)
        rnode.child.extend(node.child)
        del self.employees[node.eid]
        
    def promotion(self,eid):
        node=self.employees[eid]
        rnode=self.employees[node.report_to]
        rnode.child.remove(node)
        node.report_to=rnode.report_to
        node.designation="Manager"
        
    def traversal(self,node,depth=0):
        if node:
            print("  " * depth, node.name, node.eid)
            for j in node.child:
                self.traversal(j,depth+1)
company=Company()

ceo=Node("John",1,"CEO")
company.add_ceo(ceo)

company.add_employee(2,"Manager A","Manager", 1)
company.add_employee(3,"Manager B","Manager", 1)
company.add_employee(4,"Employee A1","Employee", 2)
company.add_employee(5,"Employee A2","Employee", 2)
company.add_employee(6,"Employee B1","Employee", 3)

print("Traversal:")
company.traversal(company.employees[1])
print()

company.resignation(5)

company.promotion(4)

company.delete_manager(2)

print("Traversal after modifications:")
company.traversal(company.employees[1])
'''
#########################################################################################################################
'''
SCENARIO-3
class CourseNode:
    def __init__(self, department, course_code, title, instructor):
        self.department = department
        self.course_code = course_code
        self.title = title
        self.instructor = instructor
        self.left = None
        self.right = None

class CourseCatalog:
    def __init__(self):
        self.root = None

    def insert_course(self, department, course_code, title, instructor):
        new_course = CourseNode(department, course_code, title, instructor)
        if self.root is None:
            self.root = new_course
        else:
            current = self.root
            while True:
                if course_code < current.course_code:
                    if current.left is None:
                        current.left = new_course
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_course
                        break
                    current = current.right

    def delete_course(self, course_code):
        # Deletion algorithm implementation

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.course_code, node.title, node.instructor)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.course_code, node.title, node.instructor)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.course_code, node.title, node.instructor)

# Usage example
catalog = CourseCatalog()
catalog.insert_course("Computer Science", "CS101", "Introduction to Programming", "Prof. Smith")
catalog.insert_course("Mathematics", "MATH201", "Calculus I", "Prof. Johnson")

# Traversal examples
catalog.inorder_traversal(catalog.root)
catalog.preorder_traversal(catalog.root)
catalog.postorder_traversal(catalog.root)
'''
