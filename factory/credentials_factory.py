from enum import Enum
from typing import Optional, TypedDict
from models.credentials import Credentials

class CredentialsDict(TypedDict):
    manufacturer: Optional[str]
    model: Optional[str]
    version: Optional[str]
    login: Optional[str]
    role: Optional[str]
    password: Optional[str]
    source: Optional[str]
    method: Optional[str]
    comment: Optional[str]
    port: Optional[str]
    
class CredentialsEnum(Enum):
    NO_DATA = "-"

class CredentialsFactory: 
    @staticmethod
    def make(params: CredentialsDict) -> Credentials:
        credentials = Credentials()
        credentials.set_manufacturer(params.get("manufacturer") or CredentialsEnum.NO_DATA.value)
        credentials.set_model(params.get("model") or CredentialsEnum.NO_DATA.value)
        credentials.set_login(params.get("login") or CredentialsEnum.NO_DATA.value)
        credentials.set_password(params.get("password") or CredentialsEnum.NO_DATA.value)
        credentials.set_role(params.get("role") or CredentialsEnum.NO_DATA.value)
        credentials.set_source(params.get("source") or CredentialsEnum.NO_DATA.value)
        credentials.set_version(params.get("version") or CredentialsEnum.NO_DATA.value)
        credentials.set_method(params.get("method") or CredentialsEnum.NO_DATA.value)
        credentials.set_comment(params.get("comment") or CredentialsEnum.NO_DATA.value)
        credentials.set_port(params.get("port") or CredentialsEnum.NO_DATA.value)
        credentials.set_address(params.get("address") or CredentialsEnum.NO_DATA.value)
        
        return credentials