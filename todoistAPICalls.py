import config as config
import requests

class ApiCalls:

    def __init__(self):
        self.apiKey = config.API_KEY
        self.headers = {
            'Authorization': f'Bearer {self.apiKey}',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.baseUrl = config.BASE_URL

    def getCallWithLimit(self, url, additionalQuery=''):

        todoistGet = requests.get(f'{self.baseUrl}{url}{additionalQuery}', headers=self.headers)
        todoistGetJson = todoistGet.json()

        nextCursor = todoistGetJson['next_cursor']
        allData = todoistGetJson['results']


        if(len(nextCursor) > 0):

            while nextCursor:
                dataHolder = requests.get(f'{self.baseUrl}{url}?cursor={nextCursor}&limit=200{additionalQuery}', headers=self.headers)
                dataHolderJson = dataHolder.json()
                allData.append(dataHolderJson['results'])
                nextCursor = dataHolderJson['next_cursor']

        return allData

    def getCallSimple(self, url, query=''):

        todoistGet = requests.get(f'{self.baseUrl}{url}{query}', headers=self.headers)
        todoistGetJson = todoistGet.json()
        return todoistGetJson

    def getAllProjects(self):
        allProjects = self.getCallSimple('projects')

        return allProjects

    def getOneProject(self,projectId):
        project = self.getCallSimple(f'projects/{projectId}')

        return project

    def getAllOpenTasks(self):
        tasks = self.getCallWithLimit('tasks')


        return tasks

    def getAllOpenTasksInAProject(self,projectId):
        tasks = self.getCallWithLimit('tasks')
        nextCursor = tasks['next_cursor']
        allData = tasks['results']


        while nextCursor:
            taskHolder = self.getCallWithLimit('tasks', f'?cursor={nextCursor}')
            allData.append(taskHolder['results'])
            nextCursor = taskHolder['next_cursor']

        return allData