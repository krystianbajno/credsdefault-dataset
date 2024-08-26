from typing import Dict, Type
from postprocessing.actions.remove_duplicates import remove_duplicates
from postprocessing.actions.sort_credentials import sort_credentials
from postprocessing.postprocessing_service import PostProcessingService

PostProcessingServiceProviderType = Dict [
    Type [
        PostProcessingService
    ], 
    PostProcessingService
]

def boot() -> PostProcessingServiceProviderType:
    actions = [
        remove_duplicates,
        lambda creds: sort_credentials(creds, "manufacturer", "model", "login"),
    ]
    
    return {
        PostProcessingService: PostProcessingService(actions),
    }
