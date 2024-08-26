from typing import List, Callable
from models.credentials import Credentials

CredentialsAction = Callable[[List[Credentials]], List[Credentials]]