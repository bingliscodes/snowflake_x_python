#company_hierarchy_node.py
import pandas as pd
from collections import defaultdict

class CompanyHierarchyNode:
    def __init__(self, name, level, parent=None):
        self.name = name
        self.level = level #'Subsidiary', 'Division', 'District', or 'Department'
        self.parent = parent
        self.children = [] #sub-units within the node
        self.personnel = [] #people associated with the node
        self.roles = defaultdict(str) #stores roles and personnel assigned to them


    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def add_personnel(self, person):
        self.personnel.append(person)

    def assign_role(self, role, person):
        """Assigns a specific role to a person at this node level."""
        # Ensure 'person' is treated as a string and check if it's not just white space
        if pd.notna(person) and person.strip():
            self.roles[role] = person

    
    def get_role(self, role):
        """Gets the person assigned to a specific role."""
        return self.roles.get(role, None)
    
    def list_roles(self):
        """Lists all roles and their assignments at this node."""
        return self.roles
    
    def find_node_by_name(self, name):
        if self.name == name:
            return self

        for child in self.children:
            result = child.find_node_by_name(name)
            
            if result is not None:
                return result

        return None
    
    #functions to find parents
    def get_subsidiary(self):
        while self.level != 'Subsidiary':
            self = self.parent

        return self.name
    
    def get_division(self):
        if self.level in ('Subsidiary'):
            return("No division at this level")
        
        while self.level != 'Division':
            self = self.parent

        return self.name

    def get_district(self):
        if self.level in ('Division', 'Subsidiary'):
            return("No district at this level")
        
        while self.level != 'District':
            self = self.parent

        return self.name
    


  

    #functions to find jobs
    def get_RVP(self): 
        if self.level == 'Subsidiary':
            return("Role does not exist at this level")
        
        while self.level != 'Division':
            self = self.parent
        
        return ('DVP (Ops): ' + self.roles['DVP (Ops)']) if self.roles['DVP (Ops)'] else None #"No DVP (Ops) found."
    
    def get_RCDD(self): 
        if self.level == 'Subsidiary':
            return("Role does not exist at this level")
        
        while self.level != 'Division':
            self = self.parent
        
        return ('DVP (Sales): ' + self.roles['DVP (Sales)']) if self.roles['DVP (Sales)'] else None #"No DVP (Sales) found."

    def get_Regional_Admin(self):
        if self.level == 'Subsidiary':
            return("Role does not exist at this level")
        
        while self.level != 'Division':
            self = self.parent

        return ('Regional Admin: ' + self.roles['Regional Admin']) if self.roles['Regional Admin'] else None #"No Regional Admin found."
    
    #For this to contiunue working we need to get the DM/MM field into the view
    def get_DoM(self):
        if self.level in ('Division', 'Subsidiary'):
            return ("Role does not exist at this level")
        
        while self.level != 'District':
            self = self.parent

        return self.roles['DOM'] if self.roles['DOM'] else None #"No DOM found."
    
    def get_Area_Manager(self):
        if self.level in ('Division', 'Subsidiary', 'District'):
            return ("Role does not exist at this level")

        return ('Area Manager: ' + self.roles['Area Manager']) if self.roles['Area Manager'] else None #"No Area Manager found."

    
    def display_hierarchy(self, level=0):
        indent = " " * level * 4
        print(f"{indent}{self.name}")
        # if self.level == 'Division':
        #     print(f"{indent}", self.get_RVP(), end = " ")
        #     print(self.get_RCDD())
        # elif self.level == 'District':
        #     print(f"{indent}", self.get_DoM())
        # elif self.level == 'Department':
        #     print(f"{indent}", self.get_Area_Manager())        
        for child in self.children:
            child.display_hierarchy(level + 1)

    def get_departments(self):
        seen = set()
        stack = [self]
        departments = []
        while stack:
            currNode = stack.pop()
            if currNode not in seen:
                seen.add(currNode)
                if currNode.level == 'Department':
                    departments.append(currNode)
                else:
                    stack.extend(currNode.children)
        
        return departments
