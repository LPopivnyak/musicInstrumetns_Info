from flask import *

app = Flask("musicInstruments_Info")
app.secret_key = "12345677890"


@app.route("/")
def mainPage():
    return render_template("index.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/Interesting_facts")
def Interesting_facts():
    return render_template("Interesting_facts.html")


app.run()