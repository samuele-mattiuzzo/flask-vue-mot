import json
import os
import urllib

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def get_mot():
    registration = request.args.get('reg')

    url = "{}{}{}".format(
        os.getenv('BASE_API_URL'),
        os.getenv('MOT_TESTS_API_URL'),
        registration
    )

    rq = urllib.request.Request(url)
    rq.add_header('x-api-key', os.getenv('API_KEY'))
    rq.add_header('Accept', 'application/json+v6')

    try:
        response = urllib.request.urlopen(rq)
        data = response.read()
        return json.loads(data)[0]
    except urllib.error.HTTPError as e:
        return jsonify(
            {'error': 'The registration is invalid or cannot be found'}
        )


if __name__ == '__main__':
    app.run()
