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
