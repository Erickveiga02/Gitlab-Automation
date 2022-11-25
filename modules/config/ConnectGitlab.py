import os
import gitlab

os.environ['GITLAB_URL'] 
gitlab_url = os.getenv('GITLAB_URL')
os.environ['GITLAB_TOKEN']
gitlab_token = os.getenv('GITLAB_TOKEN')
gl = gitlab.Gitlab(url=gitlab_url, private_token=gitlab_token,keep_base_url=True)
gl.auth()
gl.enable_debug()
