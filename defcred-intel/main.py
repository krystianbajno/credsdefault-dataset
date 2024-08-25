from collection.collection_service import CollectionService
from providers.collection_service_provider import boot as boot_collection
from providers.processing_service_provider import boot as boot_processing

from collection.collection_service import CollectionService
from processing.processing_service import ProcessingService

def main():
    collection_provider = boot_collection()
    collection_service: CollectionService = collection_provider[CollectionService.__class__]
    collected = collection_service.collect()
    
    processing_provider = boot_processing()
    processing_service: ProcessingService = processing_provider[ProcessingService.__class__]

    processed = processing_service.process(collected)

if __name__ == "__main__":
    main()