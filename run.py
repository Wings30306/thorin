import os
import json
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = "some_secret"


@app.route('/')
def index():
    image = "static/img/home-bg.jpg"
    return render_template("index.html", page_title="Thorin and Company", bgimage=image)


@app.route('/about')
def about():
    image = "static/img/about-bg.jpg"
    data = []
    with open("data/company.json", "r", encoding='utf-8') as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About the Company", company_data=data, bgimage=image)


@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    with open("data/company.json", "r", encoding='utf-8') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member, bgimage=member['image_source'])


@app.route('/contact', methods=["GET", "POST"])
def contact():
    image = "static/img/home-bg.jpg"
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(request.form["name"]))
    return render_template("contact.html", page_title="Contact us", bgimage=image)


@app.route("/careers")
def careers():
    image = "static/img/home-bg.jpg"
    return render_template("careers.html", page_title="Join our Company!", bgimage=image)


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=os.getenv("PORT"),
            debug=True)
