from typing import List, Dict
from collection.dto.intel_collection_result import IntelCollectionResult
from repository.intel_repository import IntelRepository
from collection.collector import Collector
from models.intel import Intel
from cli.messages import Messages

class CollectionService:
    def __init__(
        self, 
        collectors: Dict[str, Collector], 
        intel_repository: IntelRepository
    ):
        self.collectors: Dict[str, Collector] = collectors
        self.intel_repository: IntelRepository = intel_repository

    def collect(self) -> List[IntelCollectionResult]:
        data: List[IntelCollectionResult] = []
        
        for identifier, collector in self.collectors.items():
            if self.intel_repository.already_collected(identifier):
                collected: List[Intel] = self.intel_repository.get(identifier)
                print(Messages["repository.read_repository"](identifier))
            else:
                collected: List[Intel] = collector.run()
                self.intel_repository.save(identifier, collected)
                print(Messages["repository.save_repository"](identifier))

            data.append(IntelCollectionResult(identifier, collected))
            
        return data
