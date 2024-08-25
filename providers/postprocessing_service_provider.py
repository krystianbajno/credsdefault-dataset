from typing import Dict

from postprocessing.actions.remove_duplicates import remove_duplicates
from postprocessing.actions.sort_credentials import sort_credentials
from postprocessing.postprocessing_service import PostProcessingService

def boot() -> Dict[str, object]:
    
    actions = [
        remove_duplicates,
        lambda creds: sort_credentials(creds, "manufacturer", "model", "login"),
    ]
    
    return {
        PostProcessingService.__class__: PostProcessingService(actions),
    }
