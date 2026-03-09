import todoistAPICalls as calls
import json
import pandas as pd


api = calls.apiCalls()
projectData = api.getAllProjects()
taskData = api.getAllTasks()

for project in projectData['results']:
    print(f'Name: {project['name']}; Id: {project["id"]}')


print(len(taskData))

# if type(taskData['next_cursor']) == 'str':
#


# data_as_table = pd.DataFrame(taskData)
#
# print(data_as_table)

