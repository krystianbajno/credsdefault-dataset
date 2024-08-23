from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class CirtNet(Collector):
    def run(self) -> List[Intel]:  
        url = "https://cirt.net/passwords"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))
        data = BeautifulSoup(res.text, 'html.parser')
        td_tags = data.find_all('td')

        vendors = []
        for td in td_tags:
            a_tag = td.find('a')
            if a_tag:
                href = a_tag['href']
                vendor = a_tag['href'].split("?vendor=")[1]
                if vendor:    
                    vendors.append({
                        "href": href,
                        "vendor": vendor
                    })
        
        session = httpx.Client(base_url=url)
        
        intels = []
        vendors_len = len(vendors)
        count = 0
        for vendor in vendors:
            res = session.get(vendor["href"])
            data = BeautifulSoup(res.text, 'html.parser')
            
            pages_src = data.find_all('table')
            
            pages = []
            for page in pages_src:
                pages.append(str(page))
            
            intel = IntelFactory.make({
                "label": vendor["vendor"],
                "source": url+vendor["href"],
                "pages": pages
            })
            
            intels.append(intel)
            
            count = count + 1
            print(Messages["intel.progress"]({"intel": intel, "all": vendors_len, "count": count}))

        print(Messages["collector.collected"]({"intels": intels}))

        return intels
        