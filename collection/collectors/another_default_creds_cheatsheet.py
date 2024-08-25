# https://github.com/Edd13Mora/IoTPass/blob/main/DefaultCreds-Cheat-Sheet.csv
from typing import List
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class IoTPassDefaultCheatSheat(Collector):
    def run(self) -> List[Intel]:
        url = "https://raw.githubusercontent.com/Edd13Mora/IoTPass/main/DefaultCreds-Cheat-Sheet.csv"
        label = "IoTPassDefaultCheatSheat"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))
        
        # productvendor,username,password
        pages = res.text.split("\n")[1:]
        
        intel = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": pages,
        })
        
        print(Messages["intel.progress"]({"intel": intel, "all": 1, "count": 1}))

        intels = [intel]
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels