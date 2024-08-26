from postprocessing.postprocessing_service import PostProcessingService
from providers.collection_service_provider import CollectionServiceProviderType, boot as boot_collection
from providers.processing_service_provider import ProcessingServiceProviderType, boot as boot_processing
from providers.postprocessing_service_provider import PostProcessingServiceProviderType, boot as boot_postprocessing
from repository.credentials_fs_saver import CredentialsFsSaver

from collection.collection_service import CollectionService
from processing.processing_service import ProcessingService
from collection.dto.intel_collection_result import IntelCollectionResult

from models.credentials import Credentials

from typing import Dict, List

def main():
    collection_provider: CollectionServiceProviderType = boot_collection()
    processing_provider: ProcessingServiceProviderType = boot_processing()
    postprocessing_provider: PostProcessingServiceProviderType = boot_postprocessing()
    
    collection_service: CollectionService = collection_provider[CollectionService]
    processing_service: ProcessingService = processing_provider[ProcessingService]
    postprocessing_service: PostProcessingService = postprocessing_provider[PostProcessingService]

    collected: List[IntelCollectionResult] = collection_service.collect()
    processed: List[Credentials] = processing_service.process(collected)
    postprocessed: List[Credentials] = postprocessing_service.execute(processed)

    credentials_saver: CredentialsFsSaver = CredentialsFsSaver(filepath="output.json")
    credentials_saver.save(postprocessed)

if __name__ == "__main__":
    main()
