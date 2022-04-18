from flask import  Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html')
@app.route("/public-privacy")
def nevach():
    return render_template('public-privacy.html')


if __name__ == "__main__":
    app.run()