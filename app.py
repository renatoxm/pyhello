# import time
import random
from celery import Celery
from flask import Flask, jsonify
import os
from dotenv import load_dotenv # type: ignore
import requests

load_dotenv()

app = Flask(__name__)

# Configure Celery with Redis
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Configure Celery
def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND'],
        include=['app']
    )
    celery.conf.update(app.config)
    return celery

celery = make_celery(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# @app.route('/api-data')
# def get_api_data():
#     # API endpoint you want to access
#     url = 'https://api.gotinder.com/v2/matches?locale=pt&count=60&message=0&is_tinder_u=false'

#     api_token = os.getenv('API_TOKEN')

#     # Define your headers here
#     headers = {
#         'X-Auth-Token': api_token,
#         'Content-Type': 'application/json'
#     }

#     # Make a GET request with headers
#     response = requests.get(url, headers=headers)

#     # Check if the request was successful
#     if response.status_code == 200:
#         return jsonify(response.json())  # Return JSON response
#     else:
#         return jsonify({"error": "Failed to fetch data"}), response.status_code

@app.route('/async-api-data')
def get_async_api_data():
    delay = random.randint(10, 30)
    # Start the background task with a delay
    task = fetch_data_with_delay.apply_async(countdown=delay)  # 10-second delay before starting
    return jsonify({"status": "Task started", "task_id": task.id, "delay": delay})

@celery.task(name='app.fetch_data_with_delay')
def fetch_data_with_delay():
    # Simulate processing delay
    # time.sleep(random.randint(10, 30))  # Replace with a value between 10-30 seconds if needed
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {"error": "Failed to fetch data"}

@app.route('/task-status/<task_id>')
def get_task_status(task_id):
    task = fetch_data_with_delay.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {"status": "Pending..."}
    elif task.state == 'SUCCESS':
        response = {"status": "Completed", "data": task.result}
    else:
        response = {"status": task.state}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
