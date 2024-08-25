import json
from typing import List
from models.credentials import Credentials
from cli.messages import Messages
class CredentialsFsSaver:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, credentials: List[Credentials]):
        data = [cred.to_dict() for cred in credentials]

        with open(self.filepath, 'w') as fh:
            json.dump(data, fh, indent=4)
            print(Messages["repository.save_results"](self.filepath))