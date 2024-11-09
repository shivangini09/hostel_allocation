from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MySQL connection details
db_config = {
    'user': 'root',
    'password': 'Shivangini@09',  # Replace with your MySQL password
    'host': 'localhost',
    'database': 'hostel_management'
}

# Route for the home page
@app.route('/')
def index():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # SQL query to fetch student data
        cursor.execute("SELECT room_number, roll_number, name, batch, branch FROM students")
        students = cursor.fetchall()
        
    except Error as e:
        print(f"Error: {e}")
        students = []  # Handle errors gracefully

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()

    # Render the hostel_details.html template with student data
    return render_template("hostel_details.html", students=students)

if __name__ == '__main__':
    app.run(debug=True)

