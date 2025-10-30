from flask import Flask
import psycopg2


app = Flask(__name__)



@app.route("/user/create/<str:name>/<int:age>")
def create_user(name="", age=0):
    pass


@app.route("/user")
@app.route("/user/<int:user_id>")
def read_user(user_id=0):
    pass


@app.route("/user/<int:user_id>/update/<str:name>/<int:age>")
def receive_table(user_id=0, name="", age=0):
    pass


@app.route("user/<int:user_id>/delete")
def receive_table(user_id=0):
    pass



def create(query):
    pass

def read_update(query):
    pass

def delete(query):
    pass


