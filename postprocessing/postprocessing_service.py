from typing import List, Callable
from models.credentials import Credentials
from cli.messages import Messages

class PostProcessingService:
    def __init__(self, actions: List[Callable[[List[Credentials]], List[Credentials]]]):
        self.actions = actions

    def execute(self, credentials: List[Credentials]) -> List[Credentials]:
        print(Messages["postprocessing.entry"](credentials))
        
        for action in self.actions:
            credentials = action(credentials)
            
        print(Messages["postprocessing.exit"](credentials))
        
        return credentials

