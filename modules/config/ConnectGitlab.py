import os
import gitlab

os.environ['GITLAB_URL'] = 'http://192.168.15.200'
gitlab_url = os.getenv('GITLAB_URL')
os.environ['GITLAB_TOKEN'] = 'glpat-Z7wV3vKk1_WRvnmCWY-z'
gitlab_token = os.getenv('GITLAB_TOKEN')
gl = gitlab.Gitlab(url=gitlab_url, private_token=gitlab_token,keep_base_url=True)
gl.auth()
gl.enable_debug()