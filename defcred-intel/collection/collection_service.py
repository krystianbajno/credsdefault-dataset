from typing import List, Tuple
from repository.intel_repository import IntelRepository
from collection.collector import Collector
from models.intel import Intel
from cli.messages import Messages

class CollectionService:
    def __init__(self, collectors: List[Collector], intel_repository: IntelRepository):
        self.collectors: List[Collector] = collectors
        self.intel_repository: IntelRepository = intel_repository

    def collect(self) -> List[Tuple[str, List[Intel]]]:
        data: List[Tuple[str, List[Intel]]] = []
        
        for collector in self.collectors:
            classname: str = collector.__class__.__name__
            collected: List[Intel]
            
            if self.intel_repository.already_collected(classname):
                collected = self.intel_repository.get(classname)
                print(Messages["repository.read_repository"](classname))
            else:
                collected = collector.run()
                self.intel_repository.save(classname, collected)
                print(Messages["repository.save_repository"](classname))

            data.append((classname, collected))
            
        return data
