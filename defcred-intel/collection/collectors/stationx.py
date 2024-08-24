# https://www.stationx.net/wp-content/uploads/2015/01/defaultpassword1.csv
# Manufacturer, Model, Username, Password, Notes

from typing import List

import httpx
from collection.collector import Collector
from cli.messages import Messages
from factory.intel_factory import IntelFactory
from models.intel import Intel

class StationX(Collector):
    def run(self) -> List[Intel]:
        url = "https://www.stationx.net/wp-content/uploads/2015/01/defaultpassword1.csv"
        label = "StationX"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))
        
        # Manufactor,Product,Revision,Protocol,User ID,Password,Access,comment,Validated,Created,LastMod
        pages = res.text.split("\n")[3:]
        
        intel = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": pages,
        })
        
        print(Messages["intel.progress"]({"intel": intel, "all": 1, "count": 1}))

        intels = [intel]
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels