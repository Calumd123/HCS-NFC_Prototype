from flask import Blueprint, Flask, render_template


main = Blueprint('main', __name__)

@main.route("/", methods = ['GET'])
def home():
    return render_template("prototype.html")

@main.route("/in", methods = ['GET'])
def signedin():
    return render_template("signedin.html")

@main.route("/favicon.ico", methods = ['GET'])
def fav():
    return render_template("prototype.html")


    
