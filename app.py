from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 2,
    'title': 'Frontend Developer',
    'location': 'Remote',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 3,
    'title': 'Backend Developer',
    'location': 'Mumbai, India',
}, {
    'id': 4,
    'title': 'Data Science',
    'location': 'Delhi, India',
    'salary': 'Rs. 9,00,000'
}]


@app.route("/")
def web():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def listjobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
