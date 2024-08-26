from typing import Dict, List
from collection.dto.intel_collection_result import IntelCollectionResult
from processing.processor import Processor
from models.intel import Intel
from models.credentials import Credentials

class ProcessingService:
    def __init__(self, processors: Dict[str, Processor]):
        self.processors = processors
        
    def get_processor_for(self, entry_classname: str):
        return self.processors.get(entry_classname)

    def process(self, intel: List[IntelCollectionResult]) -> List[Credentials]:
        processed: List[Credentials] = []
        
        for entry in intel:
            processor = self.get_processor_for(entry.classname)
            if processor is None:
                continue

            data: List[Intel] = entry.intels
            credentials: List[Credentials] = processor.run(data)
            processed.extend(credentials)

        return processed
