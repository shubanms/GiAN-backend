from src.logger.loggerSetup import logger
from src.models.dataModels import reposListResponseModel
import nbformat
import requests

def getRepoList(accessToken):
    headers = {'Authorization': f'Bearer {accessToken}'}
    response = requests.get('https://api.github.com/user/repos', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        logger.info(f"Failed to fetch repository list. Status code: {response.status_code}")
        return None

def extractCodeFromIpynb(ipynbContent):
    notebook = nbformat.reads(ipynbContent.getvalue(), as_version=4)
    code_cells = [cell['source'] for cell in notebook['cells'] if cell['cell_type'] == 'code']
    return '\n'.join(code_cells)

def getRepoNames(repoList):
    reposNames = list()
    for repo in repoList:
        reposNames.append(repo['name'])
        
    responseModel = reposListResponseModel()
    
    responseModel.repos = reposNames
    
    return responseModel

