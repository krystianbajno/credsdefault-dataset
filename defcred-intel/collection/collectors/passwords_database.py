# https://www.passwordsdatabase.com

from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class PasswordsDatabase(Collector):
    def run(self) -> List[Intel]:  
        url = "https://www.passwordsdatabase.com"
        res = httpx.request("GET", url)
        
        print(Messages["collector.connected"](url))
        
        data = BeautifulSoup(res.text, 'html.parser')
        td_tags = data.find_all('td')
        intels = []
        vendors = []
        
        for td in td_tags:
            a_tag = td.find('a')
            if a_tag:
                vendor = a_tag.decode_contents()
                href = a_tag['href']
                
                if href == "http://www.netdigix.com/vancouver-it-support.php":
                    continue
               
                if vendor:    
                    vendors.append({
                        "href": href,
                        "vendor": vendor
                    })
                    
        session = httpx.Client(base_url=url)

        vendors_len = len(vendors)
        count = 0
        for vendor in vendors:
            res = session.get(vendor["href"])
            print(vendor["href"])
            data = BeautifulSoup(res.text, 'html.parser')
            
            tr = data.find_all('tr')
            tr_text = str(tr)
          
            pages = [tr_text]
                
            intel = IntelFactory.make({
                "label": vendor["vendor"],
                "source": vendor["href"],
                "pages": pages
            })
            
            intels.append(intel)
            
            count = count + 1
            print(Messages["intel.progress"]({"intel": intel, "all": vendors_len, "count": count}))
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels
        