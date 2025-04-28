from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": "1",
        "title": "Software Engineer",
        "location": "New York, United States",
        "salary": "$100,000"
    },
    {
        "id": "2",
        "title": "Frontend Engineer",
        "location": "San Francisco, United States",
        "salary": "$120,000"
    },
    {
        "id": "3",
        "title": "Backend Engineer",
        "location": "Chicago, United States",
        "salary": "$90,000"
    },
    {
        "id": "4",
        "title": "Full Stack Engineer",
        "location": "Missouri, United States",
        "salary": "$95,000"
    },
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="Nexture")

@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs);

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)