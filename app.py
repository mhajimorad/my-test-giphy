# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)
app.config["GIPHY_KEY"] = os.getenv("GIPHY_KEY")
key = app.config["GIPHY_KEY"]

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    key = os.environ.get("GIPHY_KEY")
#     #print("HEROKU!!!")
#     heroku config:set key="..."
# else:
#     app.config["GIPHY_KEY"] = os.getenv("GIPHY_KEY")
#     key = app.config["GIPHY_KEY"]

# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yourgif', methods=['GET','POST'])
def yourgif():
    query = request.form["gifchoice"]
    
    imgURL = getImageUrlFrom(query, key)
    return render_template("yourgif.html", time = datetime.now(), imgURL=imgURL)