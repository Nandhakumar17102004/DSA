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
