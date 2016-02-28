# g is a object in flask used for storing temp data. Its value is reset every request.
from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
#import sqlite3

# __name__: the name of current namespace.
app = Flask(__name__)

# # using sqlite3
# app.database = "sample.db"

# #using sqlalchemy with hard coded config
# app.secret_key = "Dboy"
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///posts.db"

# using sqlalchemy with config imported from config.py
app.config.from_object("config.DevConfig")

# create SQLAlchemy object
db = SQLAlchemy(app)

from models import *

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("You have to login first.")
            return redirect(url_for("login"))
    return wrap

@app.route("/")
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template("index_block.html", posts = posts)
#     # using sqlite3
#     g.db = connect_db()
#     cur = g.db.execute("select * from posts")
#     posts = [dict(title = row[0], description = row[1]) for row in cur.fetchall()]
#     g.db.close()
#     return render_template("index_block.html", posts = posts)
    

@app.route("/welcome")
def welcome():
    return render_template("welcome_block.html")

@app.route("/login", methods = ["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "admin":
            error = "Invalid credentials. Please check the username or password."
        else:
            session["logged_in"] = True
            flash("You were just logged in.")
            return redirect(url_for("home"))
    return render_template("login_block.html", error = error)

@app.route("/logout")
@login_required
def logout():
    session.pop("logged_in", None)
    flash("You were just logged out.")
    return redirect(url_for("welcome"))

# # using sqlite3
# def connect_db():
#     return sqlite3.connect(app.database)

if __name__ == "__main__":
    app.run(port = 8888)