from flask import *

app = Flask(__name__)


SpecialChar = ['@', '#', '$', '%', '^', '&', '/']
RestrictedChar = ['.', ',', ';', ':']

def isEmpty(username):
    if username == "":
        return "Please enter username!"
    else:
        pass

def lessThanSix(username):
    if len(username) < 6:
        return "Username should have minimum 6 characters!"
    else:
        pass
    
def greaterThanTwelve(username):
    if len(username) > 12:
        return "Username can have maximum 12 characters!"
    else:
        pass

def isAlphanumeric(username):
    if not username.isalnum():
        return "Username should be alphanumeric!"
    else:
        pass

def hasDigit(username):
    if not any(char.isdigit() for char in username):
        return "Username should have atleast one numeric character!"
    else:
        pass

def hasSpecialCharacter(username):
    if any(char in SpecialChar for char in username):
        return "Special characters are not allowed in username!"
    else:
        pass

def hasRestrictedCharacter(username):
    if any(char in RestrictedChar for char in username):
        return "Special characters are not allowed in username!"
    else:
        pass

switcher_username = [isEmpty, lessThanSix, greaterThanTwelve, hasSpecialCharacter, hasRestrictedCharacter, isAlphanumeric, hasDigit]

def isEmptyPassword(password):
    if password == "":
        return "Please enter password!"
    else:
        pass

def lessThanSixPassword(Password):
    if len(Password) < 6:
        return "Password should have minimum 6 characters!"
    else:
        pass

def greaterThanTwentyPassword(password):
    if len(password) > 20:
        return "Password can have maximum 20 characters!"
    else:
        pass

def hasDigitPassword(password):
    if not any(char.isdigit() for char in password):
        return "Password should have atleast one numeric character!"
    else:
        pass

def hasSpecialCharacterPassword(password):
    if not any(char in SpecialChar for char in password):
        return "Password should have at least one special character!"
    else:
        pass

def hasRestrictedCharacterPassword(password):
    if any(char in RestrictedChar for char in password):
        return f"Special characters from {RestrictedChar} are not allowed in password!"
    else:
        pass

switcher_password = [isEmptyPassword, lessThanSixPassword, greaterThanTwentyPassword, hasDigitPassword, hasRestrictedCharacterPassword, hasSpecialCharacterPassword]

@app.route("/login", methods = ['GET'])
def login():
    if request.method == 'GET':
        auth = request.authorization
        username = auth.username
        password = auth.password
        for item in switcher_username:
            if item(username):
                response = item(username)
                break
            elif not item(username):
                for func in switcher_password:
                    if func(password):
                        response = func(password)
                        break
                    elif not func(password):
                        response = " Login Successful!"
        return response
    

''' First, I developed the following "login" function but it had too many nested loops that could create confusions in reading the code as well as in its execution.
Hence, I moved on to develop other variants of the function.'''

# @app.route("/login", methods = ['GET'])
# def login():
#     if request.method == 'GET':
#         auth = request.authorization
#         username = auth.username
#         password = auth.password
#         SpecialChar = ['@', '#', '$', '%', '^', '&', '/']
#         if username != "":
#             if len(username) >= 6:
#                 if len(username) <=12:
#                     if username.isalnum():
#                         if any(char.isdigit() for char in username):
#                             if not any(char in SpecialChar for char in username):
#                                 if password != "":
#                                     if len(password) >= 6:
#                                         if len(password) <=20:
#                                             if any(char.isdigit() for char in password):
#                                                 if not any(char in SpecialChar for char in password):
#                                                     return "Password should have at least one special character!"
#                                                 else:
#                                                     # As there is nothing mentioned that the user will do after login
#                                                     return "Login successful!"
#                                             else:
#                                                 return "Password should have atleast one numeric character!"                                            
#                                         else:
#                                             return "Password can have maximum 20 characters!"
#                                     else:
#                                         return "Password should have minimum 6 characters!"
#                                 else:
#                                     return "Please enter password!"
#                             else:
#                                 return "Special characters are not allowed in username!"
#                         else:
#                             return "Username should have atleast one numeric character!"
#                     else:
#                         return "Username should be alphanumeric!"
#                 else:
#                     return "Username can have maximum 12 characters!"
#             else:
#                 return "Username should have minimum 6 characters!"
#         else:
#             return "Please enter username!"


'''The following "login" function is the second variant. It has a comparatively linear structure but it is still looks a bit tedious and inefficient.
That's why I moved on with building the function in a switch case format. That final function is at the first position in this code file.'''

# @app.route("/login", methods = ['GET'])
# def login():
#     if request.method == 'GET':
#         auth = request.authorization
#         username = auth.username
#         password = auth.password
#         SpecialChar = ['@', '#', '$', '%', '^', '&', '/']
#         if username == "":
#             return "Please enter username!"
#         elif len(username) < 6:
#             return "Username should have minimum 6 characters!"
#         elif len(username) > 12:
#             return "Username can have maximum 12 characters!"
#         elif not username.isalnum():
#             return "Username should be alphanumeric!"
#         elif not any(char.isdigit() for char in username):
#             return "Username should have atleast one numeric character!"
#         elif any(char in SpecialChar for char in username):
#             return "Special characters are not allowed in username!"
#         elif password == "":
#             return "Please enter password!"
#         elif len(password) < 6:
#             return "Password should have minimum 6 characters!"
#         elif len(password) > 20:
#             return "Password can have maximum 20 characters!"
#         elif not any(char.isdigit() for char in password):
#             return "Password should have atleast one numeric character!"
#         elif not any(char in SpecialChar for char in password):
#             return "Password should have at least one special character!"
#         else:
#             return "Login successful!"
        