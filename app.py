import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_reviews")
def get_reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": query}}))
    return render_template("reviews.html", reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username is already taken")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.user.insert_one(register)

        session["users"] = request.form.get("username").lower()
        flash("Registration Completed!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.user.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Oops, something was incorrect, try again!")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Oops, something was incorrect, try again!")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.user.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:    
        return render_template("profile.html", username=username)

    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You've been logged out!")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        review = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "category_name": request.form.get("category_name"),
            "about": request.form.get("about"),
            "review": request.form.get("review"),
            "image_url": request.form.get("image_url"),
            "buy_here": request.form.get("buy_here"),
            "review_by": session["user"]

        }
        mongo.db.reviews.insert_one(review)
        flash("Book Review Added!")
        return redirect(url_for("get_reviews"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_review.html", categories=categories)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        edit = {
            "book_title": request.form.get("book_title"),
            "author": request.form.get("author"),
            "category_name": request.form.get("category_name"),
            "about": request.form.get("about"),
            "review": request.form.get("review"),
            "image_url": request.form.get("image_url"),
            "buy_here": request.form.get("buy_here"),
            "review_by": session["user"]
        }
        mongo.db.reviews.update({"_id":ObjectId(review_id)}, edit)
        flash("Book Review Edited!")

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_review.html", review=review, categories=categories)


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    flash("Book Review Deleted")
    return redirect(url_for("get_reviews"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
