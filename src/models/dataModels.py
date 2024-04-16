from typing import Optional
from pydantic import BaseModel

class helloWorldInputModel(BaseModel):
    text: Optional[str] = " "
    
class helloWorldResponseModel(BaseModel):
    text: Optional[str] = " "

class authLinkInputModel(BaseModel):
    userName: Optional[str] = " "
    
class authLinkResponseModel(BaseModel):
    authLink: Optional[str] = " "

class authValidateLinkModel(BaseModel):
    authValidateLink: Optional[str] = " "

class reposListResponseModel(BaseModel):
    repos: Optional[list] = []

