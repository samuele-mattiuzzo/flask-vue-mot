# Flask Vue MOT checker

## Requirements

- Python
- Node

## Setup

- ensure VueJS is installed
  - if not run `npm install -g @vue/cli@4.5.11`
- clone the repository
- cd into the cloned folder
- create a virtual environment `python3 -m venv env`
- activate the virtual environment `source env/bin/activate`
- install the requirements `python3 -m pip install -r requirements.txt`

- in another terminal/tab:
  - `cd client`
  - `npm install`

## Running the app

- launch the Python/Flask server:

  - `python3 app.py`

- launch the Vue client:

  - `cd client`
  - `npm run serve`

- open your browser at `http://localhost:8080/mot?reg=<your reg number>`

## Tests

- cd into the project directory
- run `pytest` to run the entire test suite (tests are available under `/tests`)
