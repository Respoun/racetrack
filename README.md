# RACETRACK

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

### Explanation

Simple python/mongoDB CRUD to simulate horses races

Made for terminal

### Requirements

- docker installed
- docker-compose
- Python > 3.9

### Install

Up the database :
```bash
docker-compose up mongodb
```

Up the database UI helper :
```bash
docker-compose up mongoexpress:
```

To connect at the DB UI helper :
```bash
http://0.0.0.0:8888
```

Make sure to create a "Data" database (Or with another name but you need to change the field DATABASE_NAME in the .env file)

To connect at the DB UI helper :
```bash
http://0.0.0.0:8888
```

Creation of the virtual environment named `venv` :
```bash
virtualenv -p python3 venv
```

Activation of the environment :
```bash
source venv/bin/activate
```

Installation of dependencies :
```bash
pip install -r requirements.txt
```

Run the app :
```bash
python3 main.py
```

### Run tests

Run all the tests in /tests folder and coverage report:
```bash
coverage run -m unittest discover -s tests -p "*_test.py" && coverage report
```

See you !
