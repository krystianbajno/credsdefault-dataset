# https://github.com/Lexus89/default-passwords/blob/master/routerpasswords_portforward.csv
# https://github.com/Lexus89/default-passwords/blob/master/default-passwords_other.csv

from typing import List
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class DefaultPasswordGithubLexus(Collector):
    def run(self) -> List[Intel]:
        url = "https://raw.githubusercontent.com/Lexus89/default-passwords/master/routerpasswords_portforward.csv"
        label = "DefaultPasswordGithubLexus"
        res = httpx.request("GET", url)
        intels = []

        print(Messages["collector.connected"](url))
        
        # 100Fio Networks,Station M5,admin,admin,
        # 1net1,R-90,admin,1,
        ##2wire,1000hg,,,
        #2wire,1000s,NOLOGIN,NOLOGIN,
        #2wire,1000sw,NOLOGIN,NOLOGIN,
        #2wire,1070-B,,NOLOGIN,
        #2wire,1700hw,NOLOGIN,NOLOGIN,
        pages = res.text.split("\n")
        
        intel = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": pages,
        })
        
        intels.append(intel)
        
        print(Messages["intel.progress"]({"intel": intel, "all": 2, "count": 1}))
        
        url = "https://raw.githubusercontent.com/Lexus89/default-passwords/master/default-passwords_other.csv"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))

        # Vendor,Username,Password,Comments;
        pages = res.text.split("\n")[1:]

        intel2 = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": pages,
        })
        
        intels.append(intel2)

        print(Messages["intel.progress"]({"intel": intel, "all": 2, "count": 2}))
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels