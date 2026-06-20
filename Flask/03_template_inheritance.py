from flask import Flask,render_template

web = Flask(__name__)

@web.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    web.run(debug=True)