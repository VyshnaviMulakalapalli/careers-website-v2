from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "isrgrootx1.pem",
                       }})


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))

        jobs = []
        for row in result.all():
            jobs.append(row._asdict())

        return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"),
                              {"val": id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()


def add_application_to_db(job_id, data):
    print("Data received: ", data)
    with engine.begin() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )
        conn.execute(
            query, {
                "job_id": job_id,
                "full_name": data['full_name'],
                "email": data['email'],
                "linkedin_url": data['linkedin_url'],
                "education": data['education'],
                "work_experience": data['work_experience'],
                "resume_url": data['resume_url']
            })
        print("Data inserted successfully")


# print(type(result))
# result_all = result.all()
# print(type(result_all))
# result_all_first = result_all[0]
# print(result_all_first)
# print(type(result_all_first))
# first_element_dict = result_all_first._asdict()
# print(first_element_dict)
# print(type(first_element_dict))
