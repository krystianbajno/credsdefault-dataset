from typing import List, Callable
from models.credentials import Credentials

class PostProcessingService:
    def __init__(self, actions: List[Callable[[List[Credentials]], List[Credentials]]]):
        self.actions = actions

    def execute(self, credentials: List[Credentials]) -> List[Credentials]:
        print(f"[POSTPROCESSING] - Got {len(credentials)}")
        
        for action in self.actions:
            credentials = action(credentials)
            
        print(f"[POSTPROCESSING] - Returned total of {len(credentials)}")
        
        return credentials

