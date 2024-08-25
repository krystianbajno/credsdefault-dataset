from typing import Dict, List, Tuple
from processing.processor import Processor
from models.intel import Intel
from models.credentials import Credentials
from cli.messages import Messages

class ProcessingService:
    def __init__(self, processors: Dict[str, Processor]):
        self.processors: Dict[str, Processor] = processors

    def process(self, intel: List[Tuple[str, List[Intel]]]) -> List[Credentials]:
        data = []
        for entry in intel:
            processor: Processor = self.processors.get(entry[0])
            data: List[Intel] = entry[1]
            
            if processor is None:
                continue
            
            credentials = processor.run(data)
            
            for credential in credentials:
                data.append(credential)

        return data