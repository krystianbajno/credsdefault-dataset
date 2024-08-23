from enum import Enum
from typing import List, Optional, TypedDict
from models.intel import Intel

class IntelDict(TypedDict):
    label: Optional[str]
    source: Optional[str]
    pages: Optional[List[str]]

class IntelEnum(Enum):
    NO_DATA = "N/A"

class IntelFactory:
    @staticmethod
    def make(params: IntelDict) -> Intel:
        intel = Intel()
        intel.set_source(params.get("source") or IntelEnum.NO_DATA)
        intel.set_label(params.get("label") or IntelEnum.NO_DATA)
        intel.set_pages(params.get("pages") or [])
        
        return intel