from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class RouterPasswords(Collector):
    def run(self) -> List[Intel]:
        base_url = "https://www.routerpasswords.com"
        url = "/router-password/?router="
        res = httpx.get(base_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}, timeout=None)
        
        soup = BeautifulSoup(res.text, "html.parser")
        
        select = soup.find('select', class_="form-control")
        options = select.find_all('option')
        
        brands = [option["value"] for option in options]
        
        all_brands = len(brands)
        current = 0
        intels = []
        session = httpx.Client(base_url=base_url, follow_redirects=True)
        
        for brand in brands:
            current += 1
            current_url = url + brand
            res = session.get(current_url)
            s = BeautifulSoup(res.text, "html.parser")
              
            rows = s.find_all("tr")
            pages = []

            for row in rows:
                tds = row.find_all('td')
                if tds:
                    manufacturer = tds[0].get_text(strip=True)
                    model = tds[1].get_text(strip=True)
                    protocol = tds[2].get_text(strip=True)
                    username = tds[3].get_text(strip=True)
                    password = tds[4].get_text(strip=True)
                    
                    pages.append(f"{manufacturer}:{model}:{protocol}:{username}:{password}")

            intel = IntelFactory.make({
                "label": f"{brand}|manufacturer:model:protocol:username:password",
                "source": f"{base_url}{current_url}",
                "pages": pages
            })

            intels.append(intel)

            print(Messages["intel.progress"]({"intel": intel, "all": all_brands, "count": current}))

        print(Messages["collector.collected"]({"intels": intels}))
        
        return intels
