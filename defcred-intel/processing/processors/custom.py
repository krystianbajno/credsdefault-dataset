from typing import List
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory

class Custom(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        for intel in intels:
            for page in intel.pages:
                credentials_data = page.split(":")
                try: 
                    credential = CredentialsFactory.make({
                        "manufacturer": credentials_data[0],
                        "model": credentials_data[1],
                        "username": credentials_data[2],
                        "password": credentials_data[3],
                        "role": credentials_data[4],
                        "source": intel.source                
                    })
                    
                    credentials.append(credential)
                except:
                    continue
            
        return credentials
        
        

    