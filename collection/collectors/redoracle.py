# https://redoracle.com/PasswordDB/2wire.html

from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class RedOracle(Collector):
    def run(self) -> List[Intel]:
        base_url = "https://redoracle.com"
        url = base_url + "/PasswordDB/"
        
        res = httpx.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}, timeout=None)
        
        soup = BeautifulSoup(res.text, "html.parser")
        
        aside = soup.find('aside', class_="vp-sidebar")

        links_section = aside.find('ul', class_="vp-sidebar-links")
        links_containers = links_section.find('ul', class_="vp-sidebar-links")
        links = links_containers.find_all('a', class_="vp-link nav-link vp-sidebar-link vp-sidebar-page nav-link vp-sidebar-link vp-sidebar-page")

        scrap = []
        for link in links:
            scrap.append({
                "href": link["href"],
                "brand": link.contents[1]
            }) 
      
        session = httpx.Client(base_url=base_url)
    
        all = len(links)
        current = 0
        intels = []
        for entry in scrap:
            current = current + 1
            res = session.get(entry["href"])
            
            s = BeautifulSoup(res.text, "html.parser")
            s_res = s.find("main", class_="vp-page")
            
            intel = IntelFactory.make({
                "label": entry["brand"],
                "source": f"{base_url}/{entry["href"]}",
                "pages": [str(s_res)]
            })
            
            intels.append(intel)
            
            print(Messages["intel.progress"]({"intel": intel, "all": all, "count": current}))

        print(Messages["collector.collected"]({"intels": intels}))
        
        return intels
    
    
    
    
    
    
    
    