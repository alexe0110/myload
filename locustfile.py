from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta


class MyUser(HttpUser):
    wait_time = between(1, 5)  # Задержки между выполнением задач 1-5 seconds
    host = 'http://localhost:8000'

    def on_start(self):
        """
        Выполнятся перед началом работы, для каждого пользователя.
        """
        self.client.auth = HTTPBasicAuth(username='user', password='password')

    @task
    def get_items(self):
        self.client.get("/get_items")

    @task
    def set_item(self):
        start_time = datetime.now().astimezone().isoformat()  # Время начала, astimezone добавляет таймзону, isoformat форматирует дату в ISO 8601
        end_time = (datetime.now() + timedelta(hours=2)).astimezone().isoformat()  # Тоже самое, но добавляется дельта(=разница) времени два часа

        result = self.client.post('/add_items', data={
            'name': '123',
            'start_time': start_time,
            'end_time': end_time
        })

    @task
    def get_factorial(self):
        self.client.get("/factorial?num=22")
