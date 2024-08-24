# https://forum.ywhack.com/bountytips.php?huawei

from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

translator = {
    "预安装）/安装时自行设置（自行安装）": "Pre-installed)/Set up during installation (self-installed)",
    "随机": "random"
}

class ChinaHuawei(Collector):
    def run(self) -> List[Intel]:
        base_url = "https://forum.ywhack.com/bountytips.php?huawei"
        res = httpx.get(base_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}, timeout=None)
        intels = []
        soup = BeautifulSoup(res.text, "html.parser")

        rows = soup.find_all("tr")
        pages = []

        for row in rows:
            tds = row.find_all('td')
            if tds:
                id = tds[0].get_text(strip=True)
                family = tds[1].get_text(strip=True)
                name = tds[2].get_text(strip=True)
                typ = tds[3].get_text(strip=True)
                version = tds[4].get_text(strip=True)
                accountType = tds[5].get_text(strip=True)
                defaultUsername = tds[6].get_text(strip=True)
                defaultPassword = tds[7].get_text(strip=True)
                defaultAddress = tds[8].get_text(strip=True)

                pages.append(f"{id}:{family}:{name}:{typ}:{version}:{accountType}:{defaultUsername}:{defaultPassword}:{defaultAddress}")

        intel = IntelFactory.make({
            "label": f"ChinaHuawei|id:family:name:type:version:accountType:defaultUsername:defaultPassword:defaultAddress",
            "source": f"{base_url}",
            "pages": pages
        })

        intels.append(intel)
        
        print(Messages["collector.collected"]({"intels": intels}))
        
        return intels
