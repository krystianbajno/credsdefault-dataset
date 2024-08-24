import httpx
import string
from collection.collector import Collector
from bs4 import BeautifulSoup
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class DefPass(Collector):
    def __three_letter_combinations(self):
            letters = string.ascii_lowercase
            for first in letters:
                for second in letters:
                    for third in letters:
                        yield f"{first}{second}{third}"
                        
    def run(self):      
        url = "https://defpass.com"
        session = httpx.Client(base_url=url)
        intels = []
        combinations = list(self.__three_letter_combinations())
        all = len(combinations)
        index = 0

        for combination in combinations:
            index = index + 1
            
            res = session.post("/index.php", data={"query": combination})
            soup = BeautifulSoup(res.text, "html.parser")
            
            div = soup.find('div', {'style': 'text-align: left;color:#fff;text-shadow: 0 1px 3px rgba(0, 0, 0, .5);'})
            if div:
                content = str(div)
                intel = IntelFactory.make({
                    "label": combination,
                    "source": url,
                    "pages": [content],
                })
                
                intels.append(intel)
                print(Messages["intel.progress"]({"intel": intel, "all": all, "count": index}))
            else:
                print(f"[{index}/{all}] Not found: {combination}")
                
        print(Messages["collector.collected"]({"intels": intels}))
        
        return intels
