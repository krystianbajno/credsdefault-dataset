from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class DataRecovery(Collector):
    def run(self) -> List[Intel]:
        label = "Data-Recovery-Homepage"
        url = "https://datarecovery.com/rd/default-passwords/"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))

        data = BeautifulSoup(res.text, "html.parser")
        
        tables = data.find_all("table")
        
        pages = []
        for table in tables:
            pages.append(str(table))
        
        intel = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": [str(data)],
        })
        
        print(Messages["intel.progress"]({"intel": intel, "all": 1, "count": 1}))

        intels = [intel]
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels