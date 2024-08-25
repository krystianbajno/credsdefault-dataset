from typing import List
from models.credentials import Credentials
from models.intel import Intel
from cli.messages import Messages
class Processor:
    def run(self, intel: List[Intel]) -> List[Credentials]:
        processed = self.process(intel)
        
        print(Messages["processing.processed"]({
            "credentials": processed,
            "processor": self.__class__.__name__
        }))
        
        return processed
    
    def process(self, intels: List[Intel]) -> List[Credentials]:
        return []