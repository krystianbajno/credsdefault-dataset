from typing import List
from collection.dto.intel_collection_result import IntelCollectionResult
from repository.intel_repository import IntelRepository
from collection.collector import Collector
from models.intel import Intel
from cli.messages import Messages

class CollectionService:
    def __init__(self, collectors: List[Collector], intel_repository: IntelRepository):
        self.collectors: List[Collector] = collectors
        self.intel_repository: IntelRepository = intel_repository

    def collect(self) -> List[IntelCollectionResult]:
        data: List[IntelCollectionResult] = []
        
        for collector in self.collectors:
            classname: str = collector.__class__.__name__
            
            if self.intel_repository.already_collected(classname):
                collected: List[Intel] = self.intel_repository.get(classname)
                print(Messages["repository.read_repository"](classname))
            else:
                collected: List[Intel] = collector.run()
                self.intel_repository.save(classname, collected)
                print(Messages["repository.save_repository"](classname))

            data.append(IntelCollectionResult(classname, collected))
            
        return data