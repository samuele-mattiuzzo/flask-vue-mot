import json
import os
import urllib

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

load_dotenv()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/mot', methods=['GET'])
def get_mot():
    registration = request.args.get('reg')
    url = "https://beta.check-mot.service.gov.uk/trade/vehicles/mot-tests?registration={}".format(
        registration
    )

    rq = urllib.request.Request(url)
    rq.add_header('x-api-key', os.getenv('API_KEY'))
    rq.add_header('Accept', 'application/json+v6')

    response = urllib.request.urlopen(rq)
    data = response.read()

    return json.loads(data)[0]

    # return render_template("mot.html", details=dict["results"])


if __name__ == '__main__':
    app.run()
