import os
from todoist_api_python.api import TodoistAPI
import requests

class apiCalls:

    def __init__(self):
        self.apiKey = os.environ['TODOIST_API_KEY']
        self.api = TodoistAPI(self.apiKey)
        self.headers = {
            'Authorization': f'Bearer {self.apiKey}',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.baseUrl = 'https://api.todoist.com/api/v1/'

    def getCall(self, url):
        headers = {
            'Authorization': f'Bearer {self.apiKey}',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        todoistGet = requests.get(f'{self.baseUrl}{url}', headers=headers)
        todoistGetJson = todoistGet.json()
        return todoistGetJson


    def getAllProjects(self):
        projects = self.getCall('projects')

        return projects
