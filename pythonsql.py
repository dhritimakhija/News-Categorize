import mysql.connector

# Establish the database connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dhriti@123',
    database='userdatabase'
)

# Create a cursor object
cursor = connection.cursor()

# Insert a new user
email = 'sachinsin@gmail.com'
password = 'sachin#123'
insert_query = "INSERT INTO users (email, password) VALUES (%s, %s)"
user_data = (email, password)
cursor.execute(insert_query, user_data)

# Commit the changes and close the cursor and connection
connection.commit()
cursor.close()
connection.close()



