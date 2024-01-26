from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "vidya2812"
app.config['MYSQL_DB'] = "career"

mysql = MySQL(app)

with app.app_context():
  cur = mysql.connection.cursor()
  cur.execute("SELECT * FROM jobs")
  columns = [desc[0] for desc in cur.description]  # Get column names
  result = cur.fetchall()
  print(result)
  print(type(result))

  # Convert result into a list of dictionaries
  rows = [dict(zip(columns, row)) for row in result]
  print(rows)
