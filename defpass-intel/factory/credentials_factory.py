import enum
from typing import Optional, TypedDict
from models.credentials import Credentials

class CredentialsDict(TypedDict):
    manufacturer: Optional[str]
    model: Optional[str]
    login: Optional[str]
    role: Optional[str]
    password: Optional[str]
    
class CredentialsEnum(enum):
    NO_DATA = "N/A"

class CredentialsFactory: 
    @staticmethod
    def make(params: CredentialsDict) -> Credentials:
        credentials = Credentials()
        credentials.set_manufacturer(params.get("manufacturer") or CredentialsEnum.NO_DATA)
        credentials.set_model(params.get("model") or CredentialsEnum.NO_DATA)
        credentials.set_login(params.get("login") or CredentialsEnum.NO_DATA)
        credentials.set_password(params.get("password") or CredentialsEnum.NO_DATA)
        credentials.set_role(params.get("role") or CredentialsEnum.NO_DATA)
        
        return credentials