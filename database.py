# MySQL Connection

# from flask import Flask
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = "localhost"
# app.config['MYSQL_USER'] = "root"
# app.config['MYSQL_PASSWORD'] = "vidya2812"
# app.config['MYSQL_DB'] = "career"

# mysql = MySQL(app)

# def load_jobs_from_db():
#   with app.app_context():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM jobs")
#     columns = [desc[0] for desc in cur.description]  # Get column names
#     result = cur.fetchall()
#     # Convert result into a list of dictionaries
#     jobs = [dict(zip(columns, row)) for row in result]
#     return jobs

# def load_job_from_db(job_id):
#   with app.app_context():
#     cur = mysql.connection.cursor()
#     query = "SELECT * FROM jobs WHERE id = %s"
#     cur.execute(query, (job_id, ))
#     result = cur.fetchone()

#     if result is None:
#       return None
#     else:
#       # return the result as a dictionary
#       columns = [desc[0] for desc in cur.description]
#       job_dict = dict(zip(columns, result))
#       return job_dict

# def add_application_to_db(job_id, data):
#   with app.app_context():
#     job_id = job_id
#     full_name = data['full_name']
#     email = data['email']
#     linkedin_url = data['linkedin_url']
#     education = data['education']
#     workexperience = data['workexperience']
#     resume_url = data['resume_url']
#     cur = mysql.connection.cursor()
#     cur.execute(
#         "INSERT INTO applications(job_id, full_name, email, linkedin_url, education, workexperience, resume_url) VALUES(%s, %s, %s, %s, %s, %s, %s)",
#         (job_id, full_name, email, linkedin_url, education, workexperience,
#          resume_url))
#     mysql.connection.commit()
#     cur.close()

# MongoDB Connection

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Assuming you have initialized your MongoDB client and connected to a database
client = MongoClient('mongodb://localhost:27017/')
db = client['career']  # Assuming 'career' is the name of your MongoDB database
applications_collection = db['applications']


def load_jobs_from_db():
  jobs = list(db.jobs.find())
  return jobs


def load_job_from_db(job_id):
  job = db.jobs.find_one({'id': job_id})
  print("Loaded job:", job)
  return job


def add_application_to_db(job_id, data):
  application_document = {
      'job_id': job_id,
      'full_name': data['full_name'],
      'email': data['email'],
      'linkedin_url': data['linkedin_url'],
      'education': data['education'],
      'workexperience': data['workexperience'],
      'resume_url': data['resume_url']
  }
  applications_collection.insert_one(application_document)
