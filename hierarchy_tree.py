from collections import defaultdict
import IPython

class AccountHierarchyNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)
    
    def add_children(self, children_data):
        """Assumes children_data is a list of names for AccountHierarchyNode
        or a list of tuples (name, account_numbers) for AccountLeafNode"""
        for data in children_data:
            if isinstance(data, tuple):  # Handling leaf node data
                child_node = AccountLeafNode(data[0], data[1])
            else:  # Handling hierarchy node data
                child_node = AccountHierarchyNode(data)
            self.add_child(child_node)

    def find_child_by_name(self, name):
        """Find and return the first child with the given name."""
        for child in self.children:
            if child.name == name:
                return child
        return None  # Return None if no child with the name is found
    
    def find_category_by_account(self, account_number):
        """Find the category by account number."""
        if hasattr(self, 'account_numbers') and account_number in self.account_numbers:
            return self.name
        for child in self.children:
            result = child.find_category_by_account(account_number)
            if result:
                return result
        return None


    def display_hierarchy(self, level=0):
        indent = " " * level * 4
        print(f"{indent}{self.name}")
        for child in self.children:
            child.display_hierarchy(level + 1)

    def get_all_accounts(self):
        """Collect all account numbers from descendant leaf nodes."""
        accounts = []
        if hasattr(self, 'account_numbers'):  # Check if node is a leaf with account numbers
            accounts.extend(self.account_numbers)
        else:
            for child in self.children:
                accounts.extend(child.get_all_accounts())
        return accounts

class AccountLeafNode(AccountHierarchyNode):
    def __init__(self, name, account_numbers):
        super().__init__(name)
        self.account_numbers = account_numbers
    
    def display_hierarchy(self, level=0):
        """Override to display account numbers."""
        indent = " " * level * 4
        accounts_str = ", ".join(str(num) for num in self.account_numbers)
        print(f"{indent}{self.name}: Accounts - {accounts_str}")

DentWizard = AccountHierarchyNode("Dent Wizard")
Ebitda = AccountHierarchyNode("EBITDA")
Gross_Profit = AccountHierarchyNode("Gross Profit")
Total_SGA = AccountHierarchyNode("Total SG&A")
SGA_People = AccountHierarchyNode("SG&A - People Expenses")
SGA_Non_People = AccountHierarchyNode("SG&A - Non-People Expenses")
Net_Revenue = AccountHierarchyNode("Net Revenue")
Tech_Cost_of_Sales = AccountHierarchyNode("Tech Cost of Sales")
Gross_Revenue = AccountHierarchyNode("Gross Revenue")
Tech_Cost_of_Sales_LSR = AccountHierarchyNode("Tech COS - LSR")
Tech_Cost_of_Sales_other = AccountHierarchyNode("Tech COS - Other")
    

grossServRev = AccountLeafNode("Gross Service Revenue", ['3002000', '3003000', '3004000', '3005000', '3006000', '3007000', '3008000', '3009000', '3391000'])
otherRevenue = AccountLeafNode("Other Revenue", ['3080000', '3081000', '3082000', '3310000', '3385000', '3386000', '3388000', '3388100', '3389000', '3390000', '3392000'])
F_and_I_revenue = AccountLeafNode("F&I Revenue", ['3381000'])
Gross_Revenue_Children = [grossServRev, otherRevenue, F_and_I_revenue]

discounts = AccountLeafNode("Discounts", ['3030000', '3031000', '3032000', '3032100'])

techWages = AccountLeafNode("Tech Wages", ['4001000', '4002000', '4003000', '4004000', '4004100', '4005000'])
techBenefits = AccountLeafNode("Tech Benefits & Taxes", ['4006000', '4007000', '4008000', '4010000', '4011000', '4011200', '4013000'])
subLabor = AccountLeafNode("Sublet Labor", ['4014000'])
techCOS_LSR_Children = [techWages, techBenefits, subLabor]

techSupplies = AccountLeafNode("Tech Supplies", ['4015000', '4015500', '4016000', '4017000', '4017800', '4018000', '4018500', '4018600', '4018700', '4019000', '4020000', '4021000', '4022000', '4023000'])
techVehichle = AccountLeafNode("Tech Vehichle Expenses", ['4027000', '4028000', '4029000', '4030000', '4032000', '4033000', '4034000', '4035000'])
techTravel = AccountLeafNode("Tech Travel & Entertainment", ['4036000', '4037000', '4038000'])
techCell = AccountLeafNode("Tech Cellphones", ['4039000', '4040000'])
techOther = AccountLeafNode("Tech Other", ['4041000', '4042000', '4042500', '4043000', '4044000', '4045000', '4080000', '4081000'])
techCOS_other_Children = [techSupplies, techVehichle, techTravel, techCell, techOther]

Tech_COS_Children = [techCOS_LSR_Children, techCOS_other_Children]


SGA_wages = AccountLeafNode("SG&A Wages", ['5001000', '5002000', '5003000', '5004000', '5004500', '5005000'])
SGA_benefits = AccountLeafNode("SG&A Benefits", ['5006000', '5007000', '5008000', '5009000', '5011000', '5012000', '5013000'])
SGA_people_Children = [SGA_wages, SGA_benefits]

SGA_vehichle = AccountLeafNode("SG&A Vehichle", ['5027000', '5028000', '5029000', '5030000', '5032000', '5033000', '5034000', '5035000'])
SGA_travel = AccountLeafNode("SG&A Travel & Entertainment", ['5036000', '5037000', '5038000'])
SGA_cell = AccountLeafNode("SG&A Cellphones", ['5039000', '5040000'])
SGA_employee = AccountLeafNode("SG&A Employee Relations", ['5044000', '5045000', '5046000', '5047000', '5048000'])
SGA_supplies = AccountLeafNode("SG&A Supplies", ['5049000', '5051000', '5052000', '5053000', '5054000', '5055000', '5056000'])
SGA_facility = AccountLeafNode("SG&A Facility Expenses", ['5057000', '5058000', '5059000', '5060000', '5061000'])
SGA_advert = AccountLeafNode("SG&A Advertising & Marketing", ['5063000', '5066000', '5067000', '5068000', '5069000', '5070000', '5071000', '5072000', '5073000', '5074000', '5078000', '5078100', '5078200'])
SGA_other = AccountLeafNode("SG&A Other", [
    '5036500',
    '5041000', 
    '5079000', 
    '5080000', 
    '5081000', 
    '5082000', 
    '5083000', 
    '5084000', 
    '5085000', 
    '5086000', 
    '5087000', 
    '5088000', 
    '5089000', 
    '5089100', 
    '5090000', 
    '5091000', 
    '5095000', 
    '5096000', 
    '5097000', 
    '5098000', 
    '5099000', 
    '5100000', 
    '5100100', 
    '5101500', 
    '5102000'
    ])

SGA_non_people_Children = [SGA_vehichle, SGA_travel, SGA_cell, SGA_employee, SGA_supplies, SGA_facility, SGA_advert, SGA_other]
SGA_Children = [SGA_people_Children, SGA_non_people_Children]

DentWizard.add_child(Ebitda)
Ebitda.add_child(Gross_Profit)
Ebitda.add_child(Total_SGA)

#---------------NET REVENUE------------------
Net_Revenue.add_child(Gross_Revenue)
Net_Revenue.add_child(discounts)
Gross_Revenue.add_child(grossServRev)
Gross_Revenue.add_child(otherRevenue)
Gross_Revenue.add_child(F_and_I_revenue)
Gross_Profit.add_child(Net_Revenue)
Gross_Profit.add_child(Tech_Cost_of_Sales)
#---------------TECH COST OF SALES------------------
Tech_Cost_of_Sales.add_child(Tech_Cost_of_Sales_LSR)
Tech_Cost_of_Sales.add_child(Tech_Cost_of_Sales_other)
Tech_Cost_of_Sales_LSR.add_child(techWages)
Tech_Cost_of_Sales_LSR.add_child(techBenefits)
Tech_Cost_of_Sales_LSR.add_child(subLabor)
Tech_Cost_of_Sales_other.add_child(techSupplies)
Tech_Cost_of_Sales_other.add_child(techVehichle)
Tech_Cost_of_Sales_other.add_child(techTravel)
Tech_Cost_of_Sales_other.add_child(techCell)
Tech_Cost_of_Sales_other.add_child(techOther)

#---------------TOTAL SG&A------------------
Total_SGA.add_child(SGA_People)
Total_SGA.add_child(SGA_Non_People)
SGA_People.add_child(SGA_wages)
SGA_People.add_child(SGA_benefits)
SGA_Non_People.add_child(SGA_vehichle)
SGA_Non_People.add_child(SGA_travel)
SGA_Non_People.add_child(SGA_cell)
SGA_Non_People.add_child(SGA_employee)
SGA_Non_People.add_child(SGA_supplies)
SGA_Non_People.add_child(SGA_facility)
SGA_Non_People.add_child(SGA_advert)
SGA_Non_People.add_child(SGA_other)

def main():
    DentWizard.display_hierarchy()

if __name__ == "__main__":
    main()