import sqlite3

# Returns users' details for all companies
def getUserDetailsForAllCompanyId():
    conn = sqlite3.connect("database.db")
    companyId = conn.execute("SELECT companyId FROM company").fetchall()
    users_list = []
    for item in companyId:
        users_list.append(conn.execute('''SELECT * FROM user WHERE companyId = ?''', (item)).fetchall())
    conn.commit()
    return users_list

# print(getUserDetailsForAllCompanyId())


# Returns users' details for given companyId
def getUserDetailsForGivenCompanyId():
    conn = sqlite3.connect("database.db")
    Available_companies = conn.execute("SELECT * FROM company").fetchall()
    Available_companies_List = []
    for item in Available_companies:
        Available_companies_List.append({"companyId" : item[0], "companyName" : item[1]})
    print(f"Available companies are: {Available_companies_List}")
    companyId = input("Enter Company ID to get its users' list:(must be an integer) ")
    companyId_userList = conn.execute("SELECT companyId FROM user").fetchall()
    if companyId in str(Available_companies):
        if companyId in str(companyId_userList):
            get_data = conn.execute("SELECT * FROM user WHERE companyId = ?", (companyId)).fetchall()
            users_list = []
            for item in get_data:
                users_list.append({"userId" : item[0], "userName" : item[1], "email" : item[2], "mobile" : item[3], "password" : item[4], "companyId" : item[5]})
        else:
            return "No user is there for the given companyId!"
    else:
        return "Please enter a valid companyId!"
    conn.commit()
    return users_list

# print(getUserDetailsForGivenCompanyId())


# Returns users' details including companyName for given companyId. This function actively uses the foreign key.
def getUserDetailsAlongWithCompanyName():
    conn = sqlite3.connect("database.db")
    # Fetching details for available companies
    Available_companies = conn.execute("SELECT * FROM company").fetchall()
    Available_companies_List = []
    for item in Available_companies:
        Available_companies_List.append({"companyId" : item[0], "companyName" : item[1]})
    print(f"Available companies are: {Available_companies_List}") # Displaying the details of available companies
    # Getting companyId as input
    companyId = input("Enter Company ID to get its users' list:(must be an integer) ")
    # Fetching available companyIds from the user table
    companyId_userList = conn.execute("SELECT companyId FROM user").fetchall()
    if companyId in str(Available_companies):
        if companyId in str(companyId_userList):
            get_data = conn.execute('''SELECT user.userId, user.userName, user.email, user.mobile, user.password, user.companyId, company.companyName FROM user INNER JOIN company
              ON user.companyId = company.companyId''').fetchall()
            users_list = []
            for item in get_data:
                if item[5] == int(companyId):
                    users_list.append({"userId" : item[0], "userName" : item[1], "email" : item[2], "mobile" : item[3], "password" : item[4], "companyId" : item[5], "companyName" : item[6]})
        else:
            return "No user is there for the given companyId!"
    else:
        return "Please enter a valid companyId!"
    conn.commit()
    return users_list

# print(getUserDetailsAlongWithCompanyName())
