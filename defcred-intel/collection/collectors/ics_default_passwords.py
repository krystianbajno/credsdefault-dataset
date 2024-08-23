# https://github.com/arnaudsoullie/ics-default-passwords/blob/master/ics-default-passwords.csv

from typing import List
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class IcsDefaultPasswords(Collector):
    def run(self) -> List[Intel]:
        url = "https://raw.githubusercontent.com/arnaudsoullie/ics-default-passwords/master/ics-default-passwords.csv"
        label = "IcsDefaultPasswords"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))
        
        # Manufacturer,Model,Interface,Login,Password,Source,Comments
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