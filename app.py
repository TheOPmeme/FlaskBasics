from flask import Flask # Flask is a Class, flask is the module

app = Flask(__name__)       # __name__ is __main__  if directly accessed

@app.route("/")     # @ is a decorator, modifying function, so right now, if ever there's a "/" route, the function below runs
def home():     # can be defined as anything
    return "<h1>Hello World!</h1>"

# multiple routes can lead to the same webpage
@app.route("/best_subject")
@app.route("/propaganda")
@app.route("/Computing")
# @app.route("a")  will result in an error as all routes must begin with a /
def computing():
    return "<h1>What is Computing?</h1>"

@app.route("/a")    # also any white spaces below would not work with the web, anything written on line makes it fine

def a():    # tf it still works
     return "<h1>My apology video</h1>"


if __name__ == "__main__":
    app.run(debug=True)     # if hosted on a public server, then __name__ != __main__
