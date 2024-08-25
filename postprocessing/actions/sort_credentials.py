from typing import List
from models.credentials import Credentials

def sort_credentials(credentials: List[Credentials], *attributes) -> List[Credentials]:
    return sorted(credentials, key=lambda cred: tuple(getattr(cred, attr) for attr in attributes))