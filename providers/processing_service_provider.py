from processing.processor import Processor
from processing.processing_service import ProcessingService
from processing.processors.stationx import StationX
from processing.processors.scadapass import ScadaPass
from processing.processors.hackmd import HackMd
from processing.processors.default_creds_github_ihebski import DefaultCredsGithubIHebski
from processing.processors.another_default_creds_cheatsheet import IoTPassDefaultCheatSheat
from processing.processors.routerpasswords import RouterPasswords
from processing.processors.router_network import RouterNetwork
from processing.processors.naistroisam import NaistroiSamRu
from processing.processors.china_forumywhack import ChinaForumyWhack
from processing.processors.china_huawei import ChinaHuawei
from processing.processors.default_password_github_lexus import DefaultPasswordGithubLexus
from processing.processors.awesome_default_passwords import AwesomeDefaultPasswords
from processing.processors.custom import Custom 
from processing.processors.default_router_passwordlist import DefaultRouterPasswordsList
from processing.processors.scada_security_bootcamp import ScadaSecurityBootcamp
from processing.processors.kb_zmodo import KbZmodo
from processing.processors.ics_default_passwords import IcsDefaultPasswords
from processing.processors.many_passwords import ManyPasswords
from processing.processors.cirt_net import CirtNet
from processing.processors.defpass import DefPass
from processing.processors.data_recovery import DataRecovery

from typing import Dict, List

def boot():
    processor_instances: List[Processor] = {
        Custom(),
        DataRecovery(),
        CirtNet(),
        DefaultCredsGithubIHebski(),
        # SecLists(),
        # RouterSploitKeys(),
        # QualysPDF(),
        # PasswordsDatabase(),
        # RedOracle(),
        # Ipvm(),
        ScadaPass(),
        DefaultPasswordGithubLexus(),
        IcsDefaultPasswords(),
        ManyPasswords(),
        DefPass(),
        KbZmodo(),
        IoTPassDefaultCheatSheat(),
        AwesomeDefaultPasswords(),
        ScadaSecurityBootcamp(),
        HackMd(),
        DefaultRouterPasswordsList(),
        RouterPasswords(),
        RouterNetwork(),
        NaistroiSamRu(),
        ChinaHuawei(),
        ChinaForumyWhack(),
        StationX()
    }
    
    processors: Dict[str, Processor] = {}
    
    for processor_instance in processor_instances:
        processors[processor_instance.__class__.__name__] = processor_instance
        
    processing_service = ProcessingService(processors)
    
    return {
        ProcessingService.__class__: processing_service,
    }