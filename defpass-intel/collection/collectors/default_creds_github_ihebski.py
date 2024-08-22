from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class DefaultCredsGithubIHebski(Collector):
    def __init__(self, base_url):
        self.base_url = base_url if base_url else "https://raw.githubusercontent.com/ihebski/DefaultCreds-cheat-sheet/main/DefaultCreds-Cheat-Sheet.csv"
        self.__label = "DefaultCredsGithubIHebski"
    
    def run(self) -> List[Intel]:
        res = httpx.request("GET", self.base_url)
        print(Messages["collector.connected"](self.base_url))
        
        # productvendor,username,password
        pages = res.text.split("\n")[1:]
        
        intel = IntelFactory.make({
            "label": self.__label,
            "source": self.base_url,
            "pages": pages,
        })
        
        print(Messages["intel.progress"]({"intel": intel, "all": 1, "count": 1}))

        intels = [intel]
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels