import sqlite3

#establish a connection with sqlLite
connection=sqlite3.connect("student")

# create a cursor object to perform crud operation on student db
cursor=connection.cursor()

#create table
table_info="""
create table STUDENT( NAME VARCHAR(25), COURSE VARCHAR(25), CONTACT VARCHAR(25), GPA INT);

"""
cursor.execute(table_info)

#insert dummy data in Student table

cursor.execute('''INSERT INTO STUDENT (NAME, COURSE, CONTACT, GPA)
VALUES 
    ('Alice Johnson', 'Computer Science', '555-123-4567', 3),
    ('Bob Williams', 'Mechanical Engineering', '555-234-5678', 3),
    ('Charlie Brown', 'Electrical Engineering', '555-345-6789', 2),
    ('Diana White', 'Biology', '555-456-7890', 4),
    ('Eve Davis', 'Chemistry', '555-567-8901', 3),
    ('Frank Harris', 'Mathematics', '555-678-9012', 2),
    ('Grace Lewis', 'Physics', '555-789-0123', 3),
    ('Henry Walker', 'Economics', '555-890-1234', 3),
    ('Isabel Hall', 'History', '555-901-2345', 4),
    ('Jack Moore', 'Philosophy', '555-012-3456', 3)
               ''')
data=cursor.execute(''' Select * from STUDENT''')
for i in data:
     print(i)

#close the connection
connection.commit()
connection.close()