import sys
from pprint import pprint
from selectors import SelectSelector

import config
import todoistAPICalls as calls
import json
import pandas as pd


api = calls.ApiCalls()
projectData = api.getAllProjects()
# openTaskData = api.getAllOpenTasks()

# pprint(projectData)

projectNameInput = config.PROJECT_NAME

try:
    for project in projectData:
        if project['name'] == projectNameInput:
            projectId = project['id']
            break
except:
    print(f'Project entered not found: {projectNameInput}.  Check the name and try again.')
    sys.exit()

projectTasks = api.getAllOpenTasksInAProject(projectId)
taskList = {}
key = 1
for task in projectTasks:
    for project in projectData:
        if project['id'] == task['project_id']:
            projectName = project['name']

    taskList.update({key: {'content': task['content'], 'due': task['due'], 'labels': task['labels'], 'parent_id' : task['parent_id']}})
    key += 1


pprint(taskList)



# TODO pull out due dates, parent, project, and content
# TODO find all labels
# TODO Update past due tasks based on labels
# TODO Print out the updates tasks and new due date
# TODO create tasks based on text document including due dates, parent, project, content, labels
