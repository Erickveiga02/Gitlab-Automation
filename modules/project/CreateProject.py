import gitlab
import os
import argparse
from ..config.ConnectGitlab import gl



class ProjectCreate:

    def create_project(self):
        try:
            my_parser = argparse.ArgumentParser(description='Projeto tem como objetivo gerenciar o Gitlab através de um CLI')
            my_parser.add_argument('-p',
                                   metavar='--project',
                                   type=str,
                                   help='Nome do projeto que deseja criar')

            my_parser.add_argument('-g', metavar='--group', type=int, help='ID do groupo que deseja criar o projeto')
            args = my_parser.parse_args()
            project_name = args.p
            group = args.g
            project = gl.projects.create({'name': project_name, 'namespace_id': group})
            print("Project created")

        except gitlab.exceptions.GitlabCreateError as e:
            print("Project already exists")




