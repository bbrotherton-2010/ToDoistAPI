import todoistAPICalls as calls


api = calls.apiCalls()
projectData = api.getAllProjects()

for project in projectData['results']:
    print(project['name'])