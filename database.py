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
        result = conn.execute(
            text("select * from jobs where id = :val"),{"val":id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()


# print(type(result))
# result_all = result.all()
# print(type(result_all))
# result_all_first = result_all[0]
# print(result_all_first)
# print(type(result_all_first))
# first_element_dict = result_all_first._asdict()
# print(first_element_dict)
# print(type(first_element_dict))
