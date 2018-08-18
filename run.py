import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", page_title="Thorin and Company")

@app.route('/about')
def about():
  return render_template("about.html", page_title="About the Company")

@app.route('/contact')
def contact():
  return render_template("contact.html", page_title="Contact us")

@app.route("/careers")
def careers():
  return render_template("careers.html", page_title="Join our Company!")

if __name__ == "__main__":
  app.run(host=os.getenv("IP"),
          port=os.getenv("PORT"),
          debug=True)

