from typing import List
from models.credentials import Credentials

def remove_duplicates(credentials: List[Credentials]) -> List[Credentials]:
    unique_credentials = []
    seen = set()

    for cred in credentials:
        identifier = (
            cred.manufacturer,
            cred.model,
            cred.version,
            cred.role,
            cred.login,
            cred.password,
            cred.method,
            cred.source,
            cred.comment,
            cred.port,
            cred.address
        )

        if identifier not in seen:
            seen.add(identifier)
            unique_credentials.append(cred)

    return unique_credentials