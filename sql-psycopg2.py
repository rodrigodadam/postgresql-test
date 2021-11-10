import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursos object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table

# fetch the results (multiple)
results = cursor.fetchall()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)