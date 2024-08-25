
from typing import List

from models.intel import Intel

class IntelCollectionResult:
    def __init__(self, classname: str, intels: List[Intel]):
        self.classname: str = classname
        self.intels: List[Intel] = intels
        