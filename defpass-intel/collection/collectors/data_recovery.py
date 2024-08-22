from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.colors import Colors
from cli.messages import Messages

class DataRecovery(Collector):
    def __init__(self, base_url=None):
        self.base_url = base_url if base_url else "https://datarecovery.com/rd/default-passwords/"
        self.__label = "Data-Recovery-Homepage"
    
    def run(self) -> List[Intel]:
        res = httpx.request("GET", self.base_url)
        print(Messages["collector.connected"](self.base_url))

        data = BeautifulSoup(res.text, "html.parser")
        
        tables = data.find_all("table")
        
        pages = []
        for table in tables:
            pages.append(str(table))
        
        intel = IntelFactory.make({
            "label": self.__label,
            "source": self.base_url,
            "pages": [str(data)],
        })
        
        print(Messages["intel.progress"]({"intel": intel, "all": 1, "count": 1}))

        intels = [intel]
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels