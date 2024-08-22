from collection.collectors.data_recovery import DataRecovery
from repository.intel_repository import IntelRepository
from collection.collectors.cirt_net import CirtNet
from cli.colors import Colors
from cli.messages import Messages

def collect():
    intel_repository = IntelRepository()
    
    collectors = [
        DataRecovery("https://datarecovery.com/rd/default-passwords/"),
        CirtNet("https://cirt.net/passwords")
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
            
def process():
    pass
    

def main():
    collect()
    process()


if __name__ == "__main__":
    main()