from typing import List
from models.credentials import Credentials
from cli.messages import Messages
from .actions.credentials_action import CredentialsAction

class PostProcessingService:
    def __init__(self, actions: List[CredentialsAction]):
        self.actions = actions

    def execute(self, credentials: List[Credentials]) -> List[Credentials]:
        print(Messages["postprocessing.entry"](credentials))
        
        for action in self.actions:
            credentials = action(credentials)
            
        print(Messages["postprocessing.exit"](credentials))
        
        return credentials

