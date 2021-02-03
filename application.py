from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
def index():
    return render_template("index.html")
    
    
@application.route('/about')
def about():
    return render_template("about.html")


@application.route('/contact')
def contact():
    return render_template("contact.html")