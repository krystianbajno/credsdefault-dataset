from postprocessing.postprocessing_service import PostProcessingService
from providers.collection_service_provider import boot as boot_collection
from providers.processing_service_provider import boot as boot_processing
from providers.postprocessing_service_provider import boot as boot_postprocessing
from repository.credentials_fs_saver import CredentialsFsSaver

from collection.collection_service import CollectionService
from processing.processing_service import ProcessingService
from models.intel import Intel
from models.credentials import Credentials

from typing import Dict, List, Tuple

def main():
    collection_provider: Dict[str, object] = boot_collection()
    collection_service: CollectionService = collection_provider[CollectionService.__class__]
    
    processing_provider: Dict[str, object] = boot_processing()
    processing_service: ProcessingService = processing_provider[ProcessingService.__class__]

    postprocessing_provider: Dict[str, object] = boot_postprocessing()
    postprocessing_service: PostProcessingService = postprocessing_provider[PostProcessingService.__class__]

    collected: List[Tuple[str, List[Intel]]] = collection_service.collect()
    processed: List[Credentials] = processing_service.process(collected)
    
    processed = postprocessing_service.execute(processed)

    credentials_saver = CredentialsFsSaver(filepath="processed_credentials.json")
    credentials_saver.save(processed)

if __name__ == "__main__":
    main()
