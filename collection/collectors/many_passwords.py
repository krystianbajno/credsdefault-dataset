# https://github.com/many-passwords/many-passwords/blob/main/passwords.csv
# Vendor,Model/Software name,Version,Access Type,Username,Password,Privileges,Notes

from typing import List
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class ManyPasswords(Collector):
    def run(self) -> List[Intel]:
        url = "https://raw.githubusercontent.com/many-passwords/many-passwords/main/passwords.csv"
        label = "ManyPasswords"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))
        
        # Vendor,Model/Software name,Version,Access Type,Username,Password,Privileges,Notes
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