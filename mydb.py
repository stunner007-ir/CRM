import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Ishu@1414'
)

# Prepare cursor object
cursorObject = dataBase.cursor()

# create database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS firstdb")

print("Database created")
print("Nice Work!!")
