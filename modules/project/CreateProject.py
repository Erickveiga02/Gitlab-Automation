import gitlab
import os

from ..config.ConnectGitlab import gl

class ProjectCreate:

    def create_project(self):
        try:
            os.environ['GROUP_ID'] 
            os.environ['PROJECT_NAME'] 
            group = os.getenv('GROUP_ID')
            project_name = os.getenv('PROJECT_NAME')
            project = gl.projects.create({'name': project_name, 'namespace_id': group})
            print("Project created")

        except gitlab.exceptions.GitlabCreateError as e:
            print("Project already exists")




