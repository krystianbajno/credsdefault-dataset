# https://ipvm.com/reports/ip-cameras-default-passwords-directory

from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from factory.intel_factory import IntelFactory
from cli.messages import Messages
import html

class Ipvm(Collector):
    def run(self):      
        url = "https://ipvm.com/reports/ip-cameras-default-passwords-directory"
        
        res = httpx.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}, timeout=None)
        text = html.unescape(res.text)
        soup = BeautifulSoup(text, "html.parser")
        
        rows = soup.find_all('li')

        pages = []
        for row in rows:
            pages.append(
               row.get_text(strip=True)
            )
                
        intel = IntelFactory.make({
            "label": "ipvm",
            "pages": pages,
            "source": url
        })
        
        intels = [intel]
        print(Messages["collector.collected"]({"intels": intels}))
        
        return intels