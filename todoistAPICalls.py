import os
from pprint import pprint

from todoist_api_python.api import TodoistAPI
import requests

class apiCalls:

    def __init__(self):
        self.apiKey = os.environ['TODOIST_API_KEY']
        self.api = TodoistAPI(self.apiKey)
        self.headers = {
            'Authorization': f'Bearer {self.apiKey}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'limit': 200
        }
        self.baseUrl = 'https://api.todoist.com/api/v1/'

    def getCall(self, url, additionalQuery=''):
        headers = {
            'Authorization': f'Bearer {self.apiKey}',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        if len(additionalQuery) > 0:
            query = f'{additionalQuery}&limit=200'
        else:
            query = '?limit=200'

        todoistGet = requests.get(f'{self.baseUrl}{url}{query}', headers=headers)
        todoistGetJson = todoistGet.json()
        return todoistGetJson


    def getAllProjects(self):
        projects = self.getCall('projects')

        return projects

    def getAllOpenTasks(self):
        tasks = self.getCall('tasks')
        nextCursor = tasks['next_cursor']
        allData = tasks['results']


        while nextCursor:
            taskHolder = self.getCall('tasks', f'?cursor={nextCursor}')
            allData.append(taskHolder['results'])
            nextCursor = taskHolder['next_cursor']

        pprint(allData)
        return allData
