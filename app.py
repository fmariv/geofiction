import os

from flask import Flask, render_template

app = Flask(__name__)


try:
    GEOFICTION_ENDPOINT = os.environ['GEOFICTION_ENDPOINT']
except KeyError:
    from dotenv import load_dotenv
    load_dotenv()
    GEOFICTION_ENDPOINT = os.getenv('GEOFICTION_ENDPOINT')


@app.route("/")
def hello_world():
    return render_template('base.html')


@app.route(GEOFICTION_ENDPOINT)
def generate_fake_data():
    return "<p>This is fake data!</p>"
