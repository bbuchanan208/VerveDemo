from flask import Flask, render_template

# AWS sometimes likes "application" instead of "app", using both makes for less headaches
app = application = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('header-basic.html')


if __name__ == '__main__':
    app.run(debug=True)
