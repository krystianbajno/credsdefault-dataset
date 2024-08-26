from collection.collector import Collector
from collection.collectors.data_recovery import DataRecovery
from collection.collectors.cirt_net import CirtNet
from collection.collectors.default_creds_github_ihebski import DefaultCredsGithubIHebski
from collection.collectors.seclists import SecLists
from collection.collectors.routersploit_keys import RouterSploitKeys
from collection.collectors.scadapass import ScadaPass
from collection.collectors.default_password_github_lexus import DefaultPasswordGithubLexus
from collection.collectors.ics_default_passwords import IcsDefaultPasswords
from collection.collectors.qualys import QualysPDF
from collection.collectors.passwords_database import PasswordsDatabase
from collection.collectors.many_passwords import ManyPasswords
from collection.collectors.defpass import DefPass
from collection.collectors.custom import Custom
from collection.collectors.kb_zmodo import KbZmodo
from collection.collectors.another_default_creds_cheatsheet import IoTPassDefaultCheatSheat
from collection.collectors.awesome_default_passwords import AwesomeDefaultPasswords
from collection.collectors.stationx import StationX
from collection.collectors.scada_security_bootcamp import ScadaSecurityBootcamp
from collection.collectors.hackmd import HackMd
from collection.collectors.default_router_passwordlist import DefaultRouterPasswordsList
from collection.collectors.redoracle import RedOracle
from collection.collectors.russian_nastroyism_ru import NaistroiSamRu
from collection.collectors.ip_cameras import Ipvm
from collection.collectors.routerpasswords import RouterPasswords
from collection.collectors.router_network import RouterNetwork
from collection.collectors.china_huawei import ChinaHuawei
from collection.collectors.china_forumywhack import ChinaForumyWhack
from collection.collectors.default_password_github_lexus_other import DefaultPasswordGithubLexusOther

from collection.collection_service import CollectionService
from repository.intel_repository import IntelRepository

from typing import List

def boot():
    intel_repository = IntelRepository()
    
    collectors: List[Collector] = [
        Custom(),
        DataRecovery(),
        CirtNet(),
        DefaultCredsGithubIHebski(),
        SecLists(),
        RouterSploitKeys(),
        ScadaPass(),
        DefaultPasswordGithubLexus(),
        DefaultPasswordGithubLexusOther(),
        IcsDefaultPasswords(),
        QualysPDF(),
        PasswordsDatabase(),
        ManyPasswords(),
        DefPass(),
        KbZmodo(),
        IoTPassDefaultCheatSheat(),
        AwesomeDefaultPasswords(),
        StationX(),
        ScadaSecurityBootcamp(),
        HackMd(),
        DefaultRouterPasswordsList(),
        RedOracle(),
        NaistroiSamRu(),
        Ipvm(),
        RouterPasswords(),
        RouterNetwork(),
        ChinaHuawei(),
        ChinaForumyWhack()
    ]
    
    collection_service = CollectionService(collectors, intel_repository)
    
    return {
        IntelRepository: intel_repository,
        CollectionService: collection_service,
        "collectors": collectors,
    }