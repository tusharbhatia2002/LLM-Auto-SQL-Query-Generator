# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('test.db') 
  
# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 
  
# Creating table 
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255), MARKS INT);"""
cursor.execute(table) 
  
# Queries to INSERT records. 
cursor.execute('''Insert into STUDENT values('Tushar','Computer Science','B', 90)''') 
cursor.execute('''Insert into STUDENT values('Samridh','Software Engineering','B', 79)''') 
cursor.execute('''Insert into STUDENT values('Jaskaran','DBMS','B', 92)''') 
cursor.execute('''Insert into STUDENT values('Sarvesh','Computer Science','A', 88)''') 
cursor.execute('''Insert into STUDENT values('Peeyush','Data Science','B', 85)''') 
cursor.execute('''Insert into STUDENT values('Kanishk','IT','C', 90)''') 
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()