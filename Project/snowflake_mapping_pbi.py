from Mapping_data import *
#Takes in a list of columns in the format [snowflake name, PBI name] and returns it as a mapped list

def produce_mapping():
    for key in nameMap:
        mappingList = nameMap[key]
        print("Table name in Snowflake: ", mappingList[0][0])
        print("Table name in Power BI: ", mappingList[0][1])
        for pair in mappingList[1:]:
            print(pair[0], "-->", pair[1])

        print()
    return

produce_mapping()