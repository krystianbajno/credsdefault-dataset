# https://nastroisam.ru/router-passwords/

from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from factory.intel_factory import IntelFactory
from cli.messages import Messages
import html

class NaistroiSamRu(Collector):
    def run(self):      
        url = "https://nastroisam.ru/router-passwords/"
        
        res = httpx.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}, timeout=None)
        text = html.unescape(res.text)
        soup = BeautifulSoup(text, "html.parser")
        
        rows = soup.find_all('tr')

        extracted_data = []

        for row in rows:
            tds = row.find_all('td')
            if tds:
                manufacturer = tds[0].get_text(strip=True)
                model = tds[1].get_text(strip=True)
                login = tds[2].get_text(strip=True)
                password = tds[3].get_text(strip=True)
                
                extracted_data.append(
                    f"{model}:{manufacturer}:{login}:{password}"
                )
                    
        intel = IntelFactory.make({
            "label": "HackMd|model:manufacturer:login:password",
            "pages": extracted_data,
            "source": url
        })
        
        intels = [intel]
        print(Messages["collector.collected"]({"intels": intels}))

        return intels