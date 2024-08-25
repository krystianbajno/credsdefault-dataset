from postprocessing.postprocessing_service import PostProcessingService
from providers.collection_service_provider import boot as boot_collection
from providers.processing_service_provider import boot as boot_processing
from providers.postprocessing_service_provider import boot as boot_postprocessing
from repository.credentials_fs_saver import CredentialsFsSaver

from collection.collection_service import CollectionService
from processing.processing_service import ProcessingService
from collection.dto.intel_collection_result import IntelCollectionResult

from models.credentials import Credentials

from typing import Dict, List

def main():
    collection_provider: Dict[str, object] = boot_collection()
    processing_provider: Dict[str, object] = boot_processing()
    postprocessing_provider: Dict[str, object] = boot_postprocessing()
    
    collection_service: CollectionService = collection_provider[CollectionService.__class__]
    processing_service: ProcessingService = processing_provider[ProcessingService.__class__]
    postprocessing_service: PostProcessingService = postprocessing_provider[PostProcessingService.__class__]

    collected: List[IntelCollectionResult] = collection_service.collect()
    processed: List[Credentials] = processing_service.process(collected)
    postprocessed: List[Credentials] = postprocessing_service.execute(processed)

    credentials_saver: CredentialsFsSaver = CredentialsFsSaver(filepath="output.json")
    credentials_saver.save(postprocessed)

if __name__ == "__main__":
    main()
