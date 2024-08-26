from typing import List, Dict, Any
from collection.collection_service import CollectionService
from repository.intel_repository import IntelRepository
from .provider import load_yaml_config
from collection.collector import Collector

def boot() -> Dict[Any, Any]:
    mapping: Dict[str, List[str]] = load_yaml_config('config/processor_for_service.yaml', "mappings")
    collectors: List[Collector] = []
    
    for classname, paths in mapping.items():
        collector_path: str = paths[0]  # Extract the collector path
        
        module_name, class_name = collector_path.rsplit('.', 1)
        module = __import__(module_name, fromlist=[class_name])
        collector_class = getattr(module, class_name)
        collectors.append(collector_class())

    # You can override processor_for_service.yml:
    # collectors["CLASSNAME"] = yourimpl(yourdeps)
    
    intel_repository = IntelRepository()
    collection_service = CollectionService(collectors, intel_repository)
    
    return {
        IntelRepository: intel_repository,
        CollectionService: collection_service,
        "collectors": collectors,
    }
