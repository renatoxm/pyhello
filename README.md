# Hello World Python Project

A very simple project for testing a variety of thechnologies

- [![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
- [![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
- [![Celery](https://img.shields.io/badge/celery-%23a9cc54.svg?style=for-the-badge&logo=celery&logoColor=ddf4a4)](https://docs.celeryq.dev/)
- [Flower](https://flower.readthedocs.io/en/latest/)

## python basics

### Install Python in WSL2

#### Check if Python is installed by running

```bash
python3 --version
```

#### If not installed, update your package list and install Python

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

#### Navigate to Your Project Directory

You can access your Windows file system from WSL by navigating to /mnt/, where each drive is mounted as a folder (/mnt/c for the C drive, for example).
To move to a project directory on your C drive:

```bash
cd /mnt/c/path/to/your/project
```

#### Set Up a Virtual Environment (Recommended)

Create a virtual environment for your project:

```bash
python3 -m venv .venv
```

#### Activate the environment

```bash
source .venv/bin/activate
```

#### Deactivate the environment

```bash
deactivate
```

#### Install dependencies using pip

```bash
pip install -r requirements.txt
```

#### Run the Python Project

Now, you can run your Python project as you would in a Linux environment:

```bash
python3 app.py
```

## Celery and Redis

### Installing Redis Server on Windows with WSL2

Open your WSL2 terminal (Ubuntu or another Linux distribution).

Install Redis by running:

```bash
sudo apt update
sudo apt install redis-server
```

Start Redis and configure it to start automatically:

```bash
sudo service redis-server start
```

Verify Redis is running:

```bash
redis-cli ping
```

You should see PONG if Redis is up and running.

### Stopping Redis server

```bash
sudo service redis-server stop
```

## Running the app, flower and celery queues

You will need three separate terminal windows

run one on each (make sure python environment is active `source .venv/bin/activate`):

### start celery

```bash
celery -A app.celery worker --loglevel=info
```

### start flower

```bash
celery -A app.celery flower
```

you can access flower dashboard here: <http://localhost:5555/>

### start the app

```bash
python app.py
```

you can access your app here: <http://localhost:5000/>

<http://localhost:5000/async-api-data>

<http://localhost:5000/task-status/task-id-from-previous-route>
