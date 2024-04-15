from collections import defaultdict

nameMap = defaultdict(list)

nameMap["Transactions"] = [["REVENUE_REPORT_ROLLING_38_TRANSACTIONS", "Transactions"], ["BUNDLE_FLG", "Bundle Flag"], ["CALENDAR_CREATE_DATE", "Calendar Created Date"], ["CARMAX_CAR_TYPE", "Carmax Car Type"], ["CONTRACT_REFERENCE", "Contract Reference"], ["INVOICE_NUMBER", "Document Number"], ["HAIL_NO_HAIL_FLG", "Hail No Hail Flg"], ["INVOICE_DESCRIPTION", "Invoice Description"], ["INVOICE_TYPE", "Invoice Type"], ["KEY_TYPE_DESCRIPTION_COMBINED", "Key Type Combined"], ["PO_NUMBER", "PO Number"], ["R_O", "RO#"], ["REPAIR_ORDER_CODE", "RO# - Lines"], ["TXN_LN_RS_ITEM_DESCRIPTION", "RS Item Description"], ["SERVICE_CALENDAR_DATE", "Service Calendar Date"], ["STOCK_NUMBER", "Stock Number"], ["TXN_LN_DW_KEY_TYPE_DESCRIPTION", "Transaction Line Key Type Description"], ["TRANSACTION_TYPE", "Transaction Type"], ["TXN_LN_NOTE_DESCRIPTION", "TXN Ln Note Description"], ["VEHICLE_CONDITION", "Vehicle Condition"], ["VIN", "VIN (Transactions)"], ["INVOICE_GROSS_AMOUNT", "Invoice Gross Amount"], ["INVOICE_GROSS_AMOUNT_USD", "Invoice Gross Amount USD"],["DIM_SERVICE_INVOICE_KEY", "Dim Service Invoice Key"], ["INVOICE_LINE_NUMBER", "Invoice Line Number"]]

nameMap["Employees"] = [["REVENUE_REPORT_EMPLOYEES","Employees"],["EMPLOYEE_ADP_COMPANY", "Employee Adp Company"], ["EMPLOYEE_ADP_NUMBER", "Employee Adp Number"], ["EMPLOYEE_CERTIFICATION_LEVEL", "Employee Certification Level"], ["EMPLOYEE_CERTIFICATION_LEVEL_DATE", "Employee Certification Level Date"], ["EMPLOYEE_DEPT_DISTRICT_NAME", "Employee Dept District Name"], ["EMPLOYEE_DEPT_DISTRICT_OWNER", "Employee Dept District Owner"], ["EMPLOYEE_DEPT_NAME", "Employee Dept Name"], ["EMPLOYEE_DEPT_REGION_NAME", "Employee Dept Region Name"], ["EMPLOYEE_DEPT_SALES_MGR_FULL_NAME", "Employee Dept Sales Mgr Full Name"], ["EMPLOYEE_EMAIL", "Employee Email"], ["EMPLOYEE_FULL_NAME", "Employee Full Name"], ["EMPLOYEE_HIREDDATE", "Employee Hireddate"], ["EMPLOYEE_ID", "Employee Id"], ["EMPLOYEE_INACTIVE_FLG", "Employee Inactive Flg"], ["EMPLOYEE_JOB_GROUP", "Employee Job Group"], ["EMPLOYEE_JOB_TITLE", "Employee Job Title"], ["EMPLOYEE_LEAVE_OF_ABSENCE_FLG", "Employee Leave Of Absence Flg"], ["EMPLOYEE_REHIRE_DATE", "Employee Rehire Date"], ["EMPLOYEE_RUN_TYPE", "Employee Run Type"], ["EMPLOYEE_SUPERVISOR_ADP_NUMBER", "Employee Supervisor ADP Number"], ["EMPLOYEE_SUPERVISOR_FULL_NAME", "Employee Supervisor Full Name"], ["EMPLOYEE_TECH_CODE", "Employee Tech Code"], ["EMPLOYEE_RELEASEDATE", "Employee Term Date"], ["EMPLOYEE_TYPE", "Employee Type"], ["EMPLOYEE_DEPT_DESCRIPTION", "Employee Dept Description"]]

nameMap["Accounting_Periods"] = [["REVENUE_REPORT_ROLLING_38_ACCOUNTING_PERIOD","Accounting Periods"],["ACCNT_PERIOD_NAME", "ACCT NAME"], ["ACCNT_PERIOD_START_DATE", "Acct Period"], ["ACCNT_YEAR_FULL_NAME", "Acct Year Full Name"]]

nameMap["Transaction_Departments"] = [["REVENUE_REPORT_ROLLING_38_TRANSACTION_DEPARTMENT", "Transaction Departments"],["DEPARTMENT_DISTRICT_MGR_FULL_NAME", "Department District Mgr Full Name"], ["DEPARTMENT_DISTRICT_NAME", "Department District Name"], ["DEPARTMENT_DISTRICT_OWNER", "Department District Owner"], ["DEPARTMENT_LINE_OF_BUSINESS", "Department Line of Business"], ["DEPARTMENT_NAME", "Department Name"], ["DEPARTMENT_REGION_MGR_FULL_NAME", "Department Region Mgr Full Name"], ["DEPARTMENT_REGION_NAME", "Department Region Name"], ["DEPARTMENT_SALES_MGR_FULL_NAME", "Department Sales Mgr Full Name"]]

nameMap["Consignors"] = [["REVENUE_REPORT_ROLLING_38_COSIGNORS", "Consignors"],["CONSIGNOR_NAME", "Consignor Code"], ["CONSIGNOR_CATEGORY", "Consignor Category"], ["CONSIGNOR_DESCRIPTION", "Consignor Description"], ["PARENT_CONSIGNOR_DESCRIPTION", "Parent Consignor Description"], ["PARENT_CONSIGNOR_NAME", "Parent Consignor"]]

nameMap["Locations"] = [["REVENUE_REPORT_ROLLING_38_LOCATIONS", "Locations"], ["LOCATION_FULL_NAME", "Location Full Name"], ["TRUCK_LOCATION_TECH_CODE_NAME", "Truck Location Tech Code Name"]]

nameMap["Products"] = [["REVENUE_REPORT_ROLLING_38_PRODUCT", "Products"], ["HAIL_ITEM", "Hail Item"], ["PRODUCT_CARMAX_KEYS_CATEGORY", "Product Carmax Key Category"], ["PRODUCT_CARMAX_KEYS_TYPE", "Product Carmax Keys Type"], ["PRODUCT_DESCRIPTION", "Product Description"], ["PRODUCT_DISPLAY_NAME", "Product Display Name"], ["PRODUCT_ID", "Product Id"], ["PRODUCT_KEYS_TYPE", "Product Keys Type"], ["PRODUCT_LINE", "Product Line"], ["PRODUCT_LINE_SUBGROUP", "Product Line Subgroup"],["PRODUCT_CODE", "Items"]]

nameMap["Subsidiaries"] = [["REVENUE_REPORT_ROLLING_38_SUBSIDIARIES", "Subsidiaries"], ["SUBSIDIARY_NAME", "Subsidiary Name"]]

nameMap["Vehicles"] = [["REVENUE_REPORT_ROLLING_38_VEHICLES", "Vehicles"], ["MAKE", "Make"], ["MODEL", "Model"], ["YEAR", "Year"]]

nameMap["Sales_Channels"] = [["REVENUE_REPORT_ROLLING_38_SALES_CHANNEL", "Sales Channels"]]

nameMap["Partners"] = [["REVENUE_REPORT_ROLLING_38_PARTNERS", "Partners"]]

nameMap["Price_Level_Type"] = [["REVENUE_REPORT_ROLLING_38_PRICE_LEVEL_TYPE", "Price Level Type"], ["PRICE_LEVEL_TYPE_NAME", "Price Level Type Name"]]

nameMap["Created_Dates"] = [["REVENUE_REPORT_ROLLING_38_CREATED_DATES", "Created Dates"], ["CREATE_CALENDAR_DATE", "Create Calendar Date"]]

nameMap["Accounts"] = [["REVENUE_REPORT_ROLLING_38_ACCOUNTS", "Accounts"], ["ACCOUNT_NAME", "Account Name"], ["ACCOUNT_NUMBER", "Account Number"]]

nameMap["Service_Advisor"] = [["REVENUE_REPORT_ROLLING_38_SERVICE_ADVISOR", "Service Advisor"], ["SERVICE_ADVISOR_FULL_NAME", "Service Advisor Full Name"]]

nameMap["Insurance_Company"] = [["REVENUE_REPORT_ROLLING_38_INSURANCE_COMPANY", "Insurance Company"], ["INSURANCE_COMPANY_NAME", "Insurance Company Name"]]

nameMap["Transaction_Line_Profile"] = [["REVENUE_REPORT_ROLLING_38_TRANSACTION_LINE_PROFILE", "Transaction Line Profile"], ["KEY_TYPE_CODE", "Key Type Code"], ["KMX_KEY_CATEGORY_CODE", "KMX Key Category Code"], ["KMX_KEY_NUMBER", "KMX Key Number"], ["TRANSACTION_LINE_PROFILE_HASH", "Transaction Line Profile Hash"], ["KMX_KEY_CATEGORY_DESCRIPTION", "Transaction KMX Key Category"]]

nameMap["Customers"] = [["REVENUE_REPORT_ROLLING_38_CUSTOMERS", "Customers"], ["CUSTOMER_BILL_ADDRESS_LINE1", "Customer Bill Address Line1"], ["CUSTOMER_BILL_CITY", "Customer Bill City"], ["CUSTOMER_BILL_COUNTRY", "Customer Bill Country"], ["CUSTOMER_BILL_STATE", "Customer Bill State"], ["CUSTOMER_BILL_ZIPCODE", "Customer Bill Zipcode"], ["CUSTOMER_CATEGORY", "Customer Category"], ["CUSTOMER_COMPANY_NAME", "Customer Company Name"], ["CUSTOMER_DEALER_FRANCHISE_FLAG", "Customer Dealer Franchise Flag"], ["CUSTOMER_DEALER_HIGHLINE_FLAG", "Customer Dealer Highline Flag"], ["CUSTOMER_DEPT_NAME", "Customer Dept"], ["CUSTOMER_DEPT_DISTRICT_NAME", "Customer Dept District"], ["CUSTOMER_DEPT_DISTRICT_OWNER", "Customer Dept District Owner"], ["CUSTOMER_DEPT_LINE_OF_BUSINESS", "Customer Dept Line of Business"], ["CUSTOMER_DEPT_REGION_NAME", "Customer Dept Region"], ["CUSTOMER_DEPT_SALES_MGR_FULL_NAME", "Customer Dept Sales Mgr Full Name"], ["CUSTOMER_FLF_FLG", "Customer Flf Flg"], ["CUSTOMER_FULL_NAME", "Customer Full Name"], ["CUSTOMER_INACTIVE_FLG", "Customer Inactive Flg"], ["CUSTOMER_KMX_STORE_TYPE", "Customer KMX Store Type"], ["CUSTOMER_NUMBER", "Customer NS ID"], ["CUSTOMER_PHONE", "Customer Phone"], ["CUSTOMER_SALES_CHANNEL", "Customer Sales Channel"], ["CUSTOMER_SALESFORCE_ID_NUMBER", "Customer Salesforce ID Number"], ["CUSTOMER_SEND_TO_FI_ADMIN_FLAG", "Customer Send to FI Admin Flag"], ["CUSTOMER_SEND_TO_SALESFORCE_FLAG", "Customer Send to Salesforce Flag"], ["CUSTOMER_SEND_TO_WIZARDPRO_FLAG", "Customer Send to WizardPro Flag"], ["CUSTOMER_SHIP_ADDRESS_LINE_1", "Customer Ship Address Line 1"], ["CUSTOMER_SHIP_ADDRESS_LINE_2", "Customer Ship Address Line 2"], ["CUSTOMER_SHIP_ADDRESS_LINE_3", "Customer Ship Address Line 3"], ["CUSTOMER_SHIP_CITY", "Customer Ship City"], ["CUSTOMER_SHIP_COUNTRY_NAME", "Customer Ship Country Name"], ["CUSTOMER_SHIP_STATE_CODE", "Customer Ship State Code"], ["CUSTOMER_SHIP_STATE_NAME", "Customer Ship State Name"], ["CUSTOMER_SHIP_ZIP_CODE", "Customer Ship Zip Code"], ["CUSTOMER_SUBSIDIARY_NAME", "Customer Subsidiary Name"], ["LEVEL_2_PARENT_CUSTOMER_COMPANY_NAME", "Level 2 Parent Customer Company Name"], ["LEVEL_2_PARENT_CUSTOMER_ID", "Level 2 Parent Customer ID"], ["LEVEL_2_PARENT_CUSTOMER_NUMBER", "Level 2 Parent Customer Number"], ["LEVEL_3_PARENT_CUSTOMER_COMPANY_NAME", "Level 3 Parent Customer Company Name"], ["LEVEL_3_PARENT_CUSTOMER_ID", "Level 3 Parent Customer ID"], ["LEVEL_3_PARENT_CUSTOMER_NUMBER", "Level 3 Parent Customer Number"], ["TOP_LEVEL_1_PARENT_CUSTOMER_COMPANY_NAME", "Top Level Parent Customer Company Name"], ["TOP_LEVEL_1_PARENT_CUSTOMER_ID", "Top Level Parent Customer ID"], ["TOP_LEVEL_1_PARENT_CUSTOMER_NUMBER", "Top Level Parent Customer Number"], ["TOP_LEVEL_1_PARENT_CUSTOMER_SALES_CHANNEL", "Top Level Parent Customer Sales Channel"], ["LEVEL_4_PARENT_CUSTOMER_COMPANY_NAME", "Level 4 Parent Customer Company Name"], ["LEVEL_4_PARENT_CUSTOMER_ID", "Level 4 Parent Customer ID"], ["LEVEL_4_PARENT_CUSTOMER_NUMBER", "Level 4 Parent Customer Number"]]


