# https://192-168-1-1ip.mobi/default-router-passwords-list/
# https://192-168-1-1ip.mobi/js/parallax.js
from typing import List
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages
import json

class DefaultRouterPasswordsList(Collector):
    def run(self) -> List[Intel]:
        url = "https://192-168-1-1ip.mobi/js/parallax.js"
        label = "DefaultRouterPasswordsList"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))

        data = res.text[len("var analytics = "):].split("jQuery")[0]
        deserial = json.loads(data)
        
        # Brand Model Protocol Username Vendor
        pages = []
        for page in deserial:
            pages.append(f'{page["Brand"]}:{page["Model"]}:{page["Protocol"]}:{page["Username"]}:{page["Password"]}')
     
        intel = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": pages,
        })
        
        print(Messages["intel.progress"]({"intel": intel, "all": 1, "count": 1}))

        intels = [intel]
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels