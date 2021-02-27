from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user

from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"), code=301)

    login_user(user, remember=remember)
    return redirect(url_for("main.profile"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists")
        return redirect(url_for("auth.signup"))

    return redirect(url_for("auth.add", email=email, name=name, password=password))


@auth.route("/add")
def add():
    email = request.args["email"]
    name = request.args["name"]
    password = request.args["password"]

    return render_template("add.html", email=email, name=name, password=password)


@auth.route("/add", methods=["POST"])
def add_post():
    usr_email = request.form.get("usr-email")
    usr_name = request.form.get("usr-name")
    usr_pass = request.form.get("usr-pass")

    em_1_name = request.form.get("em-1-name")
    em_1_email = request.form.get("em-1-email")

    em_2_name = request.form.get("em-2-name")
    em_2_email = request.form.get("em-2-email")

    em_3_name = request.form.get("em-3-name")
    em_3_email = request.form.get("em-3-email")

    new_user = User(
        email=usr_email,
        name=usr_name,
        password=generate_password_hash(usr_pass, method="sha256"),
        em1name=em_1_name,
        em1email=em_1_email,
        em2name=em_2_name,
        em2email=em_2_email,
        em3name=em_3_name,
        em3email=em_3_email,
    )

    print(new_user.__dict__)

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))
