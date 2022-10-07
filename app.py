from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route("/home")
def hello_world():
    return render_template('Home.html')

@app.route("/resume")
def Resume():
    return render_template('Resume.html')

if __name__ =="__main__":
    app.run(debug=True)