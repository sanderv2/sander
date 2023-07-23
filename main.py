from flask import Flask, render_template, redirect, request
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/home", code=302)

@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return redirect("/services", code=302)
    return render_template('index.html')

@app.route('/services', methods=["GET", "POST"])
def services():
    if request.method == "POST":
        return redirect("/contact", code=302)
    return render_template('services.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    database = "./database.json"
    if request.method == "POST":
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        email = request.form.get("email")
        subject = request.form.get("subject")
        dataList = {"firstName":firstName,
                    "lastName":lastName,
                    "email":email,
                    "subject":subject}
        with open(database, "r") as f:
            temp = json.load(f)
        dataList["firstName"] = firstName
        dataList["lastName"] = lastName
        dataList["email"] = email
        dataList["subject"] = subject
        temp.append(dataList)
        with open(database, "w") as f:
            json.dump(temp, f, indent=4)
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)