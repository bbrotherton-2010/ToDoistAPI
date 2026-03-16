import todoistAPICalls as calls
import json
import pandas as pd


api = calls.apiCalls()
projectData = api.getAllProjects()
openTaskData = api.getAllOpenTasks()

for project in projectData['results']:
    print(f'Name: {project['name']}; Id: {project["id"]}')


# TODO pull out due dates, parent, project, and content
# TODO find all labels
# TODO Update past due tasks based on labels
# TODO Print out the updates tasks and new due date
# TODO create tasks based on text document including due dates, parent, project, content, labels
