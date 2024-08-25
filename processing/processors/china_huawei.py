from typing import List
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory

class ChinaHuawei(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        for intel in intels:
            for page in intel.pages:
                credentials_data = page.split(":")
                try: 
                    credential = CredentialsFactory.make({
                        "model": credentials_data[3],
                        "version": credentials_data[4],
                        "method": credentials_data[5],
                        "login": credentials_data[6],
                        "password": credentials_data[7],
                        "address": credentials_data[8],
                        "source": intel.source                
                    })
                    
                    credentials.append(credential)
                except:
                    continue
            
        return credentials
        
        

    