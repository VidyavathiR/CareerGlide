from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "vidya2812"
app.config['MYSQL_DB'] = "career"

mysql = MySQL(app)

def load_jobs_from_db():
    with app.app_context():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM jobs")
        columns = [desc[0] for desc in cur.description]  # Get column names
        result = cur.fetchall()
        # Convert result into a list of dictionaries
        jobs = [dict(zip(columns, row)) for row in result]
        # Print all rows in the form of dictionaries

        return jobs


