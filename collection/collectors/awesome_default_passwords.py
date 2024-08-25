# https://github.com/nyxxxie/awesome-default-passwords/blob/master/passwords.csv
# Manufacturer, Model, Username, Password, Notes

from typing import List

import httpx
from collection.collector import Collector
from cli.messages import Messages
from factory.intel_factory import IntelFactory
from models.intel import Intel

class AwesomeDefaultPasswords(Collector):
    def run(self) -> List[Intel]:
        url = "https://raw.githubusercontent.com/nyxxxie/awesome-default-passwords/master/passwords.csv"
        label = "AwesomeDefaultPasswords"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))
        
        # Manufacturer, Model, Username, Password, Notes
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