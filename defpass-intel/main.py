from collection.collectors.data_recovery import DataRecovery
from collection.collectors.cirt_net import CirtNet
from collection.collectors.default_creds_github_ihebski import DefaultCredsGithubIHebski
from collection.collectors.seclists import SecLists

from repository.intel_repository import IntelRepository
from cli.colors import Colors
from cli.messages import Messages

def collect():
    intel_repository = IntelRepository()
    
    collectors = [
        DataRecovery("https://datarecovery.com/rd/default-passwords/"),
        CirtNet("https://cirt.net/passwords"),
        DefaultCredsGithubIHebski("https://raw.githubusercontent.com/ihebski/DefaultCreds-cheat-sheet/main/DefaultCreds-Cheat-Sheet.csv"),
        SecLists("https://github.com")
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
            
def process(collected):
    pass

def main():
    collected = collect()
    process(collected)

if __name__ == "__main__":
    main()