from flask import Flask, render_template, request, redirect

from users_model import User
 
app = Flask(__name__)
app.secret_key = "cle"

@app.route('/')
def index_one():
    return redirect('/users')

@app.route("/users")
def index():
    list_of_users = User.get_all()
    print(list_of_users)

    return render_template("index.html", list_of_users=list_of_users)

@app.route("/users/new")
def new_user():
    return render_template("create_user.html")

@app.route("/users/create", methods = ["POST"])
def create_dog():
    User.create(request.form)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)