from typing import List

from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory

class Ipvm(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        
        for intel in intels:
            for page in intel.pages:
                content = page.split(":")
                login = None
                password = None
                if len(content) > 1:
                    split = content[1].split("/")
                    if len(split) > 1:
                        words = split[0].split(" ")
                        words2 = split[1].split(" ")
                        if not len(words) > 2 and not len(words2) > 2:
                            login = split[0]
                            password = split[1]

                    credential =  CredentialsFactory.make({
                        "manufacturer": content[0],
                        "comment": content[1],
                        "login": login,
                        "password": password
                    })
                    credentials.append(credential)
        
        return credentials
        
        

    