from flask import Flask, render_template
import random

app = Flask(__name__)

my_college = "ASRJC"
rival_college = "ACJC"
secret_text = "NIHAHAHAHAHAHAHAHAHA"
secret_nums = [111, 22, 123123, 93204920]
secret_info = {"name": "Mr Koyuki", "description": "Stupid", "gender": "women", "type": "Unknown"}

@app.route("/")
def home():
    return "<h1>Hello World!</h1>"

@app.route("/about")
def about():
    return render_template("about.html", my_college=my_college, rival_college =rival_college)    # MUST HAVE HTML FILE IN templates file

@app.route("/secret")
def secret():
    lucky_num = random.choice(secret_nums)
    return render_template("secret.html", secret_text=secret_text, lucky_num=lucky_num, secret_info=secret_info)


if __name__ == "__main__":
    app.run(debug=True, port=1234)  # a different prot number can be used, not all are available though
