from fastapi import FastAPI
from src.logger.loggerSetup import logger
from src.api.helloWorld import sayHelloWorld
from src.models.dataModels import helloWorldInputModel, authLinkInputModel, authValidateLinkModel
from src.auth.githubAuth import getGithubAuthLink, getGithubAccessToken
from src.extractor.extractor import getRepoList, getRepoNames

app = FastAPI()

logger.info("Application start-up successful!")

@app.post("/helloWorld/")
def helloWorld(inputData: helloWorldInputModel):
    helloWorldResponse = sayHelloWorld(inputData)
    
    return helloWorldResponse

@app.post("/getAuth/")
def getAuthLink(inputData: authLinkInputModel):
    authLinkResponse = getGithubAuthLink()
    
    return authLinkResponse

@app.post("/getRepos/")
def validateAuthLink(inputData: authValidateLinkModel):
    accessToken = getGithubAccessToken(inputData)
    
    reposList = getRepoList(accessToken)
    
    return getRepoNames(reposList)
