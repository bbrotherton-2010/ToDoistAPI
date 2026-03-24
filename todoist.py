import sys
from selectors import SelectSelector

import config
import todoistAPICalls as calls
import json
import pandas as pd


api = calls.ApiCalls()
projectData = api.getAllProjects()
openTaskData = api.getAllOpenTasks()

print(openTaskData)

projectNameInput = config.PROJECT_NAME

try:
    for project in projectData['results']:
        if project['name'] == projectNameInput:
            projectId = project['id']
            break
    masterList = api.getOneProject(projectId)
except:
    print(f'Project entered not found: {projectNameInput}.  Check the name and try again.')
    sys.exit()

# print(api.getAllOpenTasksInAProject(projectId))



# TODO pull out due dates, parent, project, and content
# TODO find all labels
# TODO Update past due tasks based on labels
# TODO Print out the updates tasks and new due date
# TODO create tasks based on text document including due dates, parent, project, content, labels
