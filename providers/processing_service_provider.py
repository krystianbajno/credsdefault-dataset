from typing import Dict, Any
from processing.processing_service import ProcessingService
from .provider import load_yaml_config

def boot() -> Dict[Any, Any]:
    mapping: Dict[str, list] = load_yaml_config('config/processor_for_service.yaml', "mappings")
    processors: Dict[str, object] = {}
    
    for identifier, paths in mapping.items():
        processor_path: str = paths[1]
        
        module_name, class_name = processor_path.rsplit('.', 1)
        module = __import__(module_name, fromlist=[class_name])
        processor_class = getattr(module, class_name)
        processors[identifier] = processor_class()
        
    processing_service = ProcessingService(processors)
    
    return {
        ProcessingService: processing_service,
    }
