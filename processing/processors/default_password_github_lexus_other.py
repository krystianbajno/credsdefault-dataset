from typing import List
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory

class DefaultPasswordGithubLexusOther(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        for intel in intels:
            for page in intel.pages:
                credentials_data = page.split(",")
                try: 
                    credential = CredentialsFactory.make({
                        "vendor": credentials_data[0],
                        "login": credentials_data[1],
                        "password": credentials_data[2],
                        "comment": credentials_data[3]      
                    })
                    
                    credentials.append(credential)
                except:
                    continue
            
        return credentials

    