import json
from typing import List

from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory

class RouterSploitKeys(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
                
        extract = {}
        
        for intel in intels:
            
            for page in intel.pages:
                model = intel.label.split("AUTOSCRAP_")[1]
                val = model.split(".")
                
                model = val[0]
                type = val[1]
                
                if not extract.get(model):
                    extract[model] = {}
                    
                if type == "key":
                    extract[model]["password"] = page
                
                if type == "json":
                    d = json.loads(page)
                    extract[model]["login"] = d["username"]
                    extract[model]["comment"] = d["pub_key"]
                    
                extract[model]["model"] = model

        for key, value in extract.items():
            credentials.append(CredentialsFactory.make(value))
        
        return credentials

    