from flask import Flask,render_template
import os 

web = Flask(__name__)

picpath =os.path.join('static')
web.config['UPLOAD_FOLDER'] = picpath
@web.route("/")
@web.route("/home")
def home():
    pic=os.path.join(web.config['UPLOAD_FOLDER'],'asus.jpg')  
    return  render_template("home.html",picture=pic)

@web.route("/second")
def second():
    return "Welcome to second page"

if __name__ == "__main__":
    web.run(debug=True)