class CompanyHierarchyNode:
    def __init__(self, name, level):
        self.name = name
        self.level = level #'Subsidiary', 'Division', 'District', or 'Department'
        self.children = [] #sub-units within the node
        self.personnel = [] #people associated with the node
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def add_personnel(self, person):
        self.personnel.append(person)