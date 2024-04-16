from requests_oauthlib import OAuth2Session
from src.constants import constants
from src.logger.loggerSetup import logger
from src.models.dataModels import authLinkResponseModel

def getGithubAccessToken(inputData):
    github = OAuth2Session(constants.clientId, redirect_uri=constants.redirectUri)
    token = github.fetch_token(constants.tokenUrl, authorization_response=inputData.authValidateLink, client_secret=constants.clientSecret)
    
    logger.info("Fetched token successfully!")
    
    return token['access_token']

def getGithubAuthLink():
    github = OAuth2Session(constants.clientId, redirect_uri=constants.redirectUri, scope=['repo'])
    authorizationUrl, state = github.authorization_url(constants.authorizationBaseUrl)
    logger.info("Generated the Auth link!")
    authorizationResponseModel = authLinkResponseModel()
    authorizationResponseModel.authLink = authorizationUrl
    
    return authorizationResponseModel
