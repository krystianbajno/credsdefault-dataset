import json
from typing import List
from models.credentials import Credentials

class CredentialsFsSaver:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def save(self, credentials: List[Credentials]):
        data = [self._credential_to_dict(cred) for cred in credentials]

        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def _credential_to_dict(self, credential: Credentials) -> dict:
        return {
            "manufacturer": credential.manufacturer,
            "model": credential.model,
            "version": credential.version,
            "role": credential.role,
            "login": credential.login,
            "password": credential.password,
            "method": credential.method,
            "source": credential.source,
            "comment": credential.comment,
            "port": credential.port,
            "address": credential.address
        }
