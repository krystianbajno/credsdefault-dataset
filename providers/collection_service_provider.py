from typing import Dict, Any
from collection.collection_service import CollectionService
from repository.intel_repository import IntelRepository
from .provider import load_yaml_config

def boot() -> Dict[Any, Any]:
    mapping: Dict[str, list] = load_yaml_config('config/processor_for_service.yaml', "mappings")
    collectors: Dict[str, object] = {}
    
    for identifier, paths in mapping.items():
        collector_path: str = paths[0]
        
        module_name, class_name = collector_path.rsplit('.', 1)
        module = __import__(module_name, fromlist=[class_name])
        collector_class = getattr(module, class_name)
        collectors[identifier] = collector_class()
    
    intel_repository = IntelRepository()
    collection_service = CollectionService(collectors, intel_repository)
    
    return {
        IntelRepository: intel_repository,
        CollectionService: collection_service,
        "collectors": collectors,
    }
