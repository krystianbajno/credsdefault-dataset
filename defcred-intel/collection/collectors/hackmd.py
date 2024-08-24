# https://hackmd.io/@tuBp9oxkSra7nw4TNItvUg/BkVIccr-j

from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class HackMd(Collector):
    def run(self):      
        url = "https://hackmd.io/@tuBp9oxkSra7nw4TNItvUg/BkVIccr-j"
        
        res = httpx.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}, timeout=None)

        soup = BeautifulSoup(res.text, "html.parser")
        
        rows = soup.find_all('tr', {'data-state': 'exploits'})

        extracted_data = []

        for row in rows:
            tds = row.find_all('td')
            if len(tds) == 4:
                model = tds[0].get_text(strip=True)
                manufacturer = tds[1].get_text(strip=True)
                device_type = tds[2].get_text(strip=True)
                
                credentials = tds[3].get_text(strip=True).split(':', 1)
                if len(credentials) == 2:
                    login, password = credentials
                else:
                    login = credentials[0]
                    password = "N/A" 
                
                extracted_data.append(
                    f"{model}:{manufacturer}:{device_type}:{login}:{password}"
                )
                
        intel = IntelFactory.make({
            "label": "ScadaSecurityBootcamp|model:manufacturer:device_type:login:password",
            "pages": extracted_data,
            "source": url
        })
        
        intels = [intel]
        print(Messages["collector.collected"]({"intels": intels}))

        return intels