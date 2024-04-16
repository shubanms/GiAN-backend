from src.models.dataModels import helloWorldInputModel, helloWorldResponseModel
from src.logger.loggerSetup import logger

def sayHelloWorld(inputData: helloWorldInputModel):
    response = helloWorldResponseModel()
    response.text = inputData.text
    
    logger.info(f'Response text is {response.text}')
    
    return response