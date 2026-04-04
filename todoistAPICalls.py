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

    def getCall(self, url, additionalQuery=''):

        initQuery = ''
        rerunQuery = ''

        if additionalQuery:
            initQuery = f'?{additionalQuery}'
            rerunQuery = f'&{additionalQuery}'


        todoistGet = requests.get(f'{self.baseUrl}{url}{initQuery}', headers=self.headers)
        todoistGetJson = todoistGet.json()

        nextCursor = todoistGetJson['next_cursor']
        allData = todoistGetJson['results']

        try:
            if(len(nextCursor) > 0):

                while nextCursor:
                    dataHolder = requests.get(f'{self.baseUrl}{url}?cursor={nextCursor}&limit=200{rerunQuery}', headers=self.headers)
                    dataHolderJson = dataHolder.json()
                    allData = allData + dataHolderJson['results']
                    nextCursor = dataHolderJson['next_cursor']
        except TypeError:
            pass

        return allData

    def getAllProjects(self):
        allProjects = self.getCall('projects')

        return allProjects

    def getOneProject(self,projectId):
        project = self.getCall(f'projects/{projectId}')

        return project

    def getAllOpenTasks(self):
        tasks = self.getCall('tasks')


        return tasks

    def getAllOpenTasksInAProject(self,projectId):
        tasks = self.getCall('tasks', f'project_id={projectId}')

        return tasks