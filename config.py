"""
This file acts as library to connect to
Mysql data base

"""

import mysql.connector

mydb=mysql.connector.connect(

    host='localhost',
    user='root',
    password='cherryfour22',
    database='library15'
)

#print(mydb)

mycursor=mydb.cursor()



