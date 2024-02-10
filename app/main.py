import datetime
from flask import (Flask, redirect, render_template, request, send_from_directory, url_for)

app = Flask(__name__)

@app.route('/')
def index():
    #return "Celery Stocks by Team Null"
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
   app.run()
