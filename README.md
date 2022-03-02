# Flask Vue MOT checker

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [Node/Npm](https://nodejs.org/en/)
- A MOT api key as per [documentation](https://dvsa.github.io/mot-history-api-documentation/)

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

- open your browser at `http://localhost:8080/mot?reg=<your reg number>`

## Tests

- cd into the project directory
- run `pytest` to run the entire test suite (tests are available under `/tests`)
