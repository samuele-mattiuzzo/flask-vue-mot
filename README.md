# Flask Vue MOT checker

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [Node/Npm](https://nodejs.org/en/)
- A MOT api key as per [documentation](https://dvsa.github.io/mot-history-api-documentation/)

## Structure
- The server-side aspect of the app is a python+flask application found in [app.py](app.py)
- The client is instead a vuejs app, where the main component is found in [client/src/components/Mot.vue](https://github.com/samuele-mattiuzzo/flask-vue-mot/blob/master/client/src/components/Mot.vue)
- The client uses [axios](https://www.npmjs.com/package/axios) to fire a request to the server, which in turn interrogates the MOT API endpoint using [requests](https://docs.python-requests.org/en/latest/)
- The server will always return a `200 OK` status code, even in case of empty or invalid registration number, so it can fail gracefully with a descriptive error message
- To use the app, simply visit `http://localhost:8080` and type the registration number of the vehicle that you want to check

## Setup

- ensure vuejs is installed
  - if it's not run `$ npm install -g @vue/cli@4.5.11`
- clone the repository
- cd into the project's folder

- set up the server:

  - create a virtual environment:
    - `$ python3 -m venv env`
  - activate it:
    - `$ source env/bin/activate`
  - install the requirements:
    - `$ python3 -m pip install -r requirements.txt`

- set up the client:
  - `$ cd client`
  - `$ npm install`

## Running the app

- copy `.env.example` to `.env` and add your `API_KEY` (surrounded by quotes)
- in two separate terminal tabs:

  - launch the server:

    - `$ source env/bin/activate`
    - `$ python3 app.py`

  - launch the client:

    - `$ cd client`
    - `$ npm run serve`

- open your browser at `http://localhost:8080`

## Tests

- `$ python3 tests.py`
