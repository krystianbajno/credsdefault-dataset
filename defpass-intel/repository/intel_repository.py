import json
import os
from typing import List
from models.intel import Intel

class IntelRepository:
    def __serialize_intels(self, intels: List[Intel]) -> str:
        intels_dict = [intel.to_dict() for intel in intels]
        return json.dumps(intels_dict)

    def __deserialize_intels(self, serialized_data: str) -> List[Intel]:
        intels_dict = json.loads(serialized_data)
        return list([Intel.from_dict(data) for data in intels_dict])

    def get(self, classname) ->  List[Intel]:
        with open(f"data/{classname}.json", "r") as hout:
            deserialized = self.__deserialize_intels(hout.read())
            return deserialized
        
    def save(self, classname, intels: List[Intel]) -> None:
        with open(f"data/{classname}.json", "w") as hout:
            serialized = self.__serialize_intels(intels)
            hout.write(serialized)
        
    def already_collected(self, classname): 
        return os.path.exists(f"data/{classname}.json")
    