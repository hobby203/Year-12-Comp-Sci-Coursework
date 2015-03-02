import sys
import sqlite3
from Student import Student


class DBMS:
    def __init__(self, reset):
        self.conn = sqlite3.connect('merit.db')
        self.cursor = self.conn.cursor()
        if reset:
            self.db_reset()

    def db_reset(self):
        self.conn.execute("DROP TABLE IF EXISTS Classes")

        self.conn.execute("DROP TABLE IF EXISTS Students")

        self.conn.execute("DROP TABLE IF EXISTS Teachers")

        self.conn.execute("CREATE TABLE Classes ("
                          "class_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                          "class_name VARCHAR(5) NOT NULL)")

        self.conn.execute("CREATE TABLE Students (" +
                          "student_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                          "class_id INTEGER NOT NULL,"
                          "first_name VARCHAR(50) NOT NULL,"
                          "surname VARCHAR(50) NOT NULL,"
                          "merits INTEGER NOT NULL,"
                          "FOREIGN KEY (class_id) REFERENCES Classes(class_id))")

        self.conn.execute("CREATE TABLE Teachers ("
                          "teacher_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                          "class_id INTEGER NOT NULL,"
                          "first_name VARCHAR(50) NOT NULL,"
                          "surname VARCHAR(50) NOT NULL,"
                          "FOREIGN KEY (class_id) REFERENCES Classes(class_id))")

        self.conn.commit()

    def add_user(self, username, first_name, second_name):  # Add user method
        # New object called user, so i can reference the things i've just put into it like user.username

        user = Student(username, first_name, second_name)
        return user

    # Returns a new object called user, with the information of the student. Needs work, will use a query to find the
    # username specified and return values dependant on what it finds.
    def find_user(self, username, first_name, second_name):
        user = Student(username, first_name,
                       second_name)
        return user

    def run(self):  # A method which would run queries for me, so i could have done mysql().run(BLARGH)
        try:  # Again try the query, and return a error with the errors arguments
            self.cursor.execute("SELECT firstName FROM testforDj")

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        while (1):

            row = self.cursor.fetchone()

            for i in int(self.cursor.rowcount):
                print row[i]
                print "Number of rows returned: %d" % self.cursor.rowcount

            if row == None:
                break