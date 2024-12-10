import mysql.connector

mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "admin",
    password = "FinalTest0000!",
    database = "dbfinal"
)

# database driver bikin dulu dor check the database driver
mycursor = mydb.cursor()
def show_table_simple(table_name):
    try:
        query = f"SELECT * FROM {table_name}"  # Query to fetch all rows
        mycursor.execute(query)  # Execute the query
        results = mycursor.fetchall()  # Fetch all rows

        if results:
            for row in results:
                print(row)  # Print each row
        else:
            print(f"Table '{table_name}' is empty.")
    except Exception as e:
        print(f"Error: {e}")


show_table_simple("car")