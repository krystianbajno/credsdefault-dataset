
from typing import List

from models.intel import Intel

class IntelCollectionResult:
    def __init__(self, identifier: str, intels: List[Intel]):
        self.identifier: str = identifier
        self.intels: List[Intel] = intels
        