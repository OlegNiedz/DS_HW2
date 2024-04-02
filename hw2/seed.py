import faker
from random import randint, choice
import psycopg2
from create_tables import db_connect


def generate_fake_data(NUMBER_USERS=7, NUMBER_TASKS=30) -> tuple:
    fake_users = []  # тут зберігатимемо КОРИСТУВАЧІВ
    fake_tasks = []  # тут зберігатимемо ЗАДАЧІ
    statuses = [("new",), ("in progress",), ("completed",)]

    fake_data = faker.Faker()

    # Створимо набір користувачів у кількості
    for _ in range(NUMBER_USERS):
        fake_users.append((fake_data.name(), fake_data.email()))

    # Згенеруємо тепер набір задач
    for _ in range(NUMBER_TASKS):
        fake_tasks.append(
            (   f"delivery to {fake_data.address()}",
                f"customer: {fake_data.company()}",
                randint(1, 3),
                randint(1, NUMBER_USERS),
            )
        )

    return statuses, fake_users, fake_tasks


def fill_tbl(db_connection, tbl_name="", columns="", values=[]):
    sql_str = f"INSERT INTO {tbl_name}({columns}) VALUES ({('%s,'*len(columns.split(",")))[:-1:]})"

    cursor = db_connection.cursor()
    cursor.executemany(sql_str, values)
    cursor.close()


def main():
    db_connection = db_connect()

    fake_data = generate_fake_data()
    fill_tbl(
        db_connection=db_connection,
        tbl_name="status",
        columns="name",
        values=fake_data[0],
    )
    fill_tbl(
        db_connection=db_connection,
        tbl_name="users",
        columns="fullname, email",
        values=fake_data[1],
    )
    fill_tbl(
        db_connection=db_connection,
        tbl_name="tasks",
        columns="title, description, status_id, user_id",
        values=fake_data[2],
    )

    db_connection.commit()
    db_connection.close()


if __name__ == "__main__":
    main()
