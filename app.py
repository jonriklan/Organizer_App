from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return "<H1>Home Page</H1>"

@app.route("/about")
def about_page():
    return "<H1>About Page</H1>"


if __name__ == '__main__':
    app.run()