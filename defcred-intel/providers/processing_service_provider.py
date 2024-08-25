from processing.processor import Processor
from processing.processing_service import ProcessingService

from processing.processors.stationx import StationX
from processing.processors.scadapass import ScadaPass

from typing import Dict

def boot():
    processors: Dict[str, Processor] = {
        # Custom(),
        # DataRecovery(),
        # CirtNet(),
        # DefaultCredsGithubIHebski(),
        # SecLists(),
        # RouterSploitKeys(),
        ScadaPass.__name__: ScadaPass(),
        # DefaultPasswordGithubLexus(),
        # IcsDefaultPasswords(),
        # QualysPDF(),
        # PasswordsDatabase(),
        # ManyPasswords(),
        # DefPass(),
        # KbZmodo(),
        # IoTPassDefaultCheatSheat(),
        # AwesomeDefaultPasswords(),
        # ScadaSecurityBootcamp(),
        # HackMd(),
        # DefaultRouterPasswordsList(),
        # RedOracle(),
        # NaistroiSamRu(),
        # Ipvm(),
        # RouterPasswords(),
        # RouterNetwork(),
        # ChinaHuawei(),
        # ChinaForumyWhack(),
        StationX.__name__: StationX()

    }
    
    processing_service = ProcessingService(processors)
    
    return {
        ProcessingService.__class__: processing_service,
        "processors": processors,
    }