# Ashley Williamson 8th December 2011
# Fixed by Daniel Burnley because what is this

from System import System

# It takes the username and password, the beginning information from the login method


# def getMoreInfo(username, password):
#     firstName = raw_input("What is your firstName? ")  # Assigns firstName and secondName to some raw_inputs
#     secondName = raw_input("What is your secondName? ")
#
#     # Creates the user object, since addUser returns the object, user now becomes the user object. Snazzy no?
#     user = mysqlObj.addUser(username, firstName,
#                             secondName)
#
#     # LOVELY FOR LOOP! It basically goes through the attrib names like username, firstName and
#     # then the values for each, by iterating through each in the user object
#     for attr, value in user.__dict__.iteritems():
#         # Rather hacky way, normally used in debuggers, but it'll suffice
#
#         # Some if statements so formatting looks nice, instead of firstName Ashley, it's First Name: Ashley
#         if attr == (
#                 "username"):
#             attr = "Username"  # Now assign the attrib of this iteration a fancier looking name!
#
#         elif attr == ("firstName"):
#             attr = "First Name"
#         else:
#             attr = "Second Name"
#
#         # The print statement to print the attr which we made fancier, then have a nice : and then the value!
#         # Having it add : here instead of above says 1 char per string!
#         print attr + ": " + value.capitalize()
#
#
# # function responsible for just checking the information and returns 1 or -1 dependant on the result!
# def checkUser(username, password):
#     if (username.isalnum()) and (username.isalnum()):
#         if (username == "06williamsona") and (
#                     password == "ohyeah"):  # If both fields match we'll return 1 saying that yes it's valid,
#             return 1  # see
#         else:  # otherwise
#             print "Incorrect"  # We'll tell them it's wrong so they know what's going on
#             return -1  # And we'll throw -1, so the method login knows that i needs to ask them again!
#     else:
#         print "You have invalid characters within your username and/or password, please try again."
#         return -1
#
#
# def exit():
#     print "Thankyou for using the school system"
#     if (MysqlObj.commit()):  # Commit changes to the database
#         print "Changes commited to the database"
#     if (MysqlObj.cursor.close()):  # Close the cursor object
#         print "Cursor Closed"
#     if (MysqlObj.connect.close()):  # Close the mysql conenction
#         print "Connection Closed"


# Deprecated
# mysqlObj = Mysql()
#
# if (mysqlObj):
#
#     invalid = True
#
#     while invalid == True:
#
#         username = raw_input("Username: ")  #Initial call for information
#         password = getpass.getpass()
#
#         if checkUser(username, password) >= 1:
#             invalid = False
#             print "Invalid is now equal to,", str(invalid)
#             #getMoreInfo(username,password)
#
#             #query = raw_input("Please enter a query: ")
#             mysqlObj.run()
#
#
#
#         ## CHECKS OUT, DO SOME MORE STUFF

if __name__ == "__main__":
    System()
