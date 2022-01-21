from flask import Flask, render_template, request, redirect

from users_model import User
 
app = Flask(__name__)
app.secret_key = "cle"

@app.route('/')
@app.route("/users")
def index():
    # users = User.get_all()
    # return render_template("index.html", users=users)
    return render_template("index.html", users=User.get_all())

@app.route("/users/new")
def new_user():
    return render_template("create_user.html")

@app.route("/users/create", methods = ["POST"])
def create_user():
    User.create(request.form)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)