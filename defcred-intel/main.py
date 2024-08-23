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
from repository.intel_repository import IntelRepository
from models.intel import Intel
from typing import List

from cli.messages import Messages

def collect() -> List[Intel]:
    intel_repository = IntelRepository()
    
    collectors: List[Collector] = [
        DataRecovery(),
        CirtNet(),
        DefaultCredsGithubIHebski(),
        SecLists(),
        RouterSploitKeys(),
        ScadaPass(),
        DefaultPasswordGithubLexus(),
        IcsDefaultPasswords(),
        QualysPDF(),
        PasswordsDatabase(),
        ManyPasswords(),
        DefPass(),
        Custom()
    ]
    
    data = []
    for collector in collectors:
        classname = collector.__class__.__name__
        
        if intel_repository.already_collected(classname):
            collected = intel_repository.get(classname)
            print(Messages["repository.read_repository"](classname))
        else:
            collected = collector.run()
            intel_repository.save(classname, collected)
            print(Messages["repository.save_repository"](classname))

        data.append((classname, collected))
            
def process(collected) -> None:
    pass

def main():
    collected = collect()
    process(collected)

if __name__ == "__main__":
    main()