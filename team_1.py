from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")

def fmain():
    return render_template("index.html")

iff __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)

# Simulating a change to test GitHub Actions | Test 111
