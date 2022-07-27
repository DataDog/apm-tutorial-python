from datetime import datetime, timedelta
from random import randint
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the calendar app!"


@app.route('/calendar')
def getDate():
    "Generates a random date in 2022."

    day_offset = randint(0, 365)
    start_date = datetime(2022, 1, 1)
    output = start_date + timedelta(days=day_offset)
    print(output)
    return output.strftime("%m/%d/%Y")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)