#from hierarchy_tree import *
from collections import defaultdict
#This file will maintain the account hierarchy to allow us to put individual expenses into buckets based on the account number

#we will use a dictionary of dictionaries, starting at the smallest level
hierarchyMap = defaultdict(str)

grossServRev = ['3002000', '3003000', '3004000', '3005000', '3006000', '3007000', '3008000', '3009000', '3391000']
otherRevenue = ['3080000', '3081000', '3082000', '3310000', '3385000', '3386000', '3388000', '3388100', '3389000', '3390000', '3392000']
F_and_I_revenue = ['3381000']
Gross_Revenue = [grossServRev, otherRevenue, F_and_I_revenue]

discounts = ['3030000', '3031000', '3032000', '3032100']

techWages = ['4001000', '4002000', '4003000', '4004000', '4004100', '4005000']
techBenefits = ['4006000', '4007000', '4008000', '4009000', '4010000', '4011000', '4011200', '4013000']
subLabor = ['4014000']
techCOS_LSR = [techWages, techBenefits, subLabor]

techSupplies = ['4015000', '4015500', '4016000', '4017000', '4017800', '4018000', '4018500', '4018600', '4018700', '4019000', '4020000', '4021000', '4022000', '4023000']
techVehichle = ['4027000', '4028000', '4029000', '4030000', '4031000', '4032000', '4033000', '4034000', '4035000']
techTravel = ['4036000', '4037000', '4038000']
techCell = ['4039000', '4040000']
techOther = ['4041000', '4042000', '4042500', '4043000', '4044000', '4045000', '4080000', '4081000']
techCOS_other = [techSupplies, techVehichle, techTravel, techCell, techOther]

Tech_COS = [techCOS_LSR, techCOS_other]


SGA_wages = ['5001000', '5002000', '5003000', '5004000', '5004500', '5005000']
SGA_benefits = ['5006000', '5007000', '5008000', '5009000', '5011000', '5012000', '5013000']
SGA_people = [SGA_wages, SGA_benefits]

SGA_vehichle = ['5027000', '5028000', '5029000', '5030000', '5031000', '5032000', '5033000', '5034000', '5035000']
SGA_travel = ['5036000', '5037000', '5038000']
SGA_cell = ['5039000', '5040000']
SGA_employee = ['5044000', '5045000', '5046000', '5047000', '5048000']
SGA_supplies = ['5049000', '5051000', '5052000', '5053000', '5054000', '5055000', '5056000']
SGA_facility = ['5057000', '5058000', '5059000', '5060000', '5061000']
SGA_advert = ['5063000', '5066000', '5067000', '5068000', '5069000', '5070000', '5071000', '5072000', '5073000', '5074000', '5078000', '5078100', '5078200']
SGA_other = [
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
]

SGA_non_people = [SGA_vehichle, SGA_travel, SGA_cell, SGA_employee, SGA_supplies, SGA_facility, SGA_advert, SGA_other]
SGA = [SGA_people, SGA_non_people]


