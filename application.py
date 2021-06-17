from flask import Flask, render_template

# AWS sometimes likes "application" instead of "app", using both makes for less headaches
app = application = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# Normally I wouldn't create three separate routes, but this will allow me to link the pages with the buttons and no
# additional arguments
@app.route('/full')
def full():
    context = {
        "battery_percent": 100,
        "hours_remaining": "12",
        "minutes_remaining": "00",
        "firmware_needs_update": False,
        "maintenance_needed": False,
    }
    return render_template('dashboard.html', context=context)


@app.route('/low')
def low():
    context = {
        "battery_percent": 20,
        "hours_remaining": "2",
        "minutes_remaining": "24",
        "firmware_needs_update": True,
        "maintenance_needed": False,
    }
    return render_template('dashboard.html', context=context)


@app.route('/very_low')
def very_low():
    context = {
        "battery_percent": 6,
        "hours_remaining": "0",
        "minutes_remaining": "43",
        "firmware_needs_update": True,
        "maintenance_needed": True,
    }
    return render_template('dashboard.html', context=context)


if __name__ == '__main__':
    app.run(debug=False)
