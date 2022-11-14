import gitlab
import os
os.environ['GITLAB_URL'] = 'http://192.168.15.200'
gitlab_url = os.getenv('GITLAB_URL')
os.environ['GITLAB_TOKEN'] = 'glpat-Z7wV3vKk1_WRvnmCWY-z'
gitlab_token = os.getenv('GITLAB_TOKEN')
gl = gitlab.Gitlab(url=gitlab_url, private_token=gitlab_token,keep_base_url=True)
gl.auth()
gl.enable_debug()
class ProjectCreate:

    def create_project(self):
        try:
            os.environ['GROUP_ID'] = '4'
            os.environ['PROJECT_NAME'] = 'Createproject-erick'
            group = os.getenv('GROUP_ID')
            project_name = os.getenv('PROJECT_NAME')
            project = gl.projects.create({'name': project_name, 'namespace_id': group})
            print("Project created")

        except gitlab.exceptions.GitlabCreateError as e:
            print("Project already exists")






