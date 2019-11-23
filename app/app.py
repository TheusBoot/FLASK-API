from flask import Flask

app = Flask(__name__)



@app.route("/")
def index():
    return "Hello World!"



""" (segurança, só vai da run caso for o o principal)"""
if __name__ == "__main__":
    app.run()
