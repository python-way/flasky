from . import main

@main.route("/")
def hello():
    return "<h1>HELLO THERE!</h1>"

