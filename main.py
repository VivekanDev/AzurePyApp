from flask import Flask

app = Flask(__name__)

app.route("/")
def homepage():
  return "<h2>Python Flask app is Running !</h2>"

if __name__=="__main__":
  app.run()
