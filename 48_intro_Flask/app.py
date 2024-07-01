from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/time')
def current_time():
    now = datetime.now()  # get the current time
    time_string = now.strftime("%H:%M:%S")  # format time as a string
    return f"Current Time: {time_string}"

if __name__ == '__main__':
    app.run(debug=True)
