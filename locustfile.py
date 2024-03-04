from locust import HttpUser, task, between
from requests.auth import HTTPBasicAuth


class MyUser(HttpUser):
    wait_time = between(1, 5)   # Задержки между выполнением задач 1-5 seconds
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
    def get_factorial(self):
        self.client.get("/factorial?num=22")

