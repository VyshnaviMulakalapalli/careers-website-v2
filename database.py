from sqlalchemy import create_engine
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "isrgrootx1.pem",
                       }})

# print(type(result))
# result_all = result.all()
# print(type(result_all))
# result_all_first = result_all[0]
# print(result_all_first)
# print(type(result_all_first))
# first_element_dict = result_all_first._asdict()
# print(first_element_dict)
# print(type(first_element_dict))
