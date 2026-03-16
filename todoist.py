import todoistAPICalls as calls
import json
import pandas as pd


api = calls.apiCalls()
projectData = api.getAllProjects()
openTaskData = api.getAllOpenTasks()

for project in projectData['results']:
    print(f'Name: {project['name']}; Id: {project["id"]}')



