import psycopg2

sql_delete_tbls = """
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS USERS;
DROP TABLE IF EXISTS status;
"""

sql_create_table_users = """
-- Table: USERS
--DROP TABLE IF EXISTS USERS;
CREATE TABLE USERS (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
"""
sql_create_table_status = """
-- Table: status
--DROP TABLE IF EXISTS status;
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
"""
sql_create_table_tasks = """
-- Table: tasks
--DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id int REFERENCES status(id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    user_id int 
      REFERENCES users(id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);
"""


def db_connect(
    database="",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port=5432,
):
    return psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port,
    )


if __name__ == "__main__":
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute(sql_delete_tbls)
    cursor.execute(sql_create_table_status)
    cursor.execute(sql_create_table_users)
    cursor.execute(sql_create_table_tasks)
    connection.commit()
    cursor.close()
    connection.close()
