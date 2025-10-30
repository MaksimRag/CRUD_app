from flask import Flask
import psycopg2
import json


app = Flask(__name__)



@app.route("/")
def start_slash():
    return "CRUD_app"


@app.route("/user/create/<string:name>/<int:age>")
def create_user(name="", age=0):
    query = f"""INSERT INTO "Users" (name, age) VALUES ('{name}', {age});"""
    create_delete(query=query)
    query = """SELECT * FROM "Users" ORDER BY user_id DESC LIMIT 1;"""
    user = read_update(query=query)
    return f"Пользователь - добавлен {user}"


@app.route("/users")
def users_reade():
    query = """SELECT * FROM "Users";"""
    users = read_update(query=query)
    return users


@app.route("/user/<int:user_id>")
def user_reade(user_id=0):
    query = f"""SELECT * FROM "Users" WHERE user_id = {user_id};"""
    user = read_update(query=query)
    return user


@app.route("/user/<int:user_id>/update/<string:name>/<int:age>")
def user_update(user_id=0, name="", age=0):
    query = f"""UPDATE "Users" SET name = {name}, age = {age} WHERE user_id = {user_id};"""
    user = read_update(query=query)
    return user


@app.route("/user/<int:user_id>/delete")
def receive_table(user_id=0):
    query = f"""DELETE FROM "Users" WHERE user_id = {user_id};"""
    create_delete(query=query)
    return f"Пользователь {user_id} - удалён"



def create_delete(query):
    try:
        connection = psycopg2.connect(database="CRUD_app", user="postgres", password="admin", host="localhost", port="5432")
        cursor = connection.cursor()
        cursor.execute(query=query)
        connection.commit()

        cursor.close()
        connection.close()

    except Exception as error:
        print(f"Ошибка: {error}".encode('utf-8', errors='replace').decode())


def read_update(query):
    try:
        connection = psycopg2.connect(database="CRUD_app", user="postgres", password="admin", host="localhost", port="5432")
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        result = []
        for row in rows:
            result.append(dict(zip(columns, row)))
        query_answer = json.dumps(result, ensure_ascii=False, indent=4)
        query_answer = json.loads(query_answer)

        cursor.close()
        connection.close()

        return result

    except Exception as error:
        print(f"Ошибка: {error}".encode('utf-8', errors='replace').decode())



if __name__ == "__main__":
    app.run()
