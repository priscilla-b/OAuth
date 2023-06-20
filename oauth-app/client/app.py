import os

from dotenv import load_dotenv
from flask import (
    Flask,
    flash, 
    render_template, 
    redirect,
    request,
    url_for,
)


load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route("/", methods=["GET"])
def index():
   
    return render_template("./index.html")

@app.route("/login", methods=["GET"])
def login():
   
    return render_template("./login.html")


if __name__ == '__main__':
    app.run()