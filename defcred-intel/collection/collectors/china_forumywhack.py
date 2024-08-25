from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages
import time

class ChinaForumyWhack(Collector):
    def run(self) -> List[Intel]:
        endpoint = "/password.php"
        base_url = "https://forum.ywhack.com"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
        intels = []

        res = httpx.get(base_url + endpoint, headers=headers, timeout=None)
        soup = BeautifulSoup(res.text, "html.parser")
        
        pages_div = soup.find("div", class_="pages")
        if pages_div:
            last_page_link = pages_div.find_all('a')[-2]
            all_pages = int(last_page_link.text.strip())
        else:
            all_pages = 457  

        current_page = 1
        
        session = httpx.Client(base_url=base_url, headers=headers, timeout=None)
        while current_page <= all_pages:
            try:
                req_url = f"{endpoint}?page={current_page}"
                page_url = f"{base_url}{req_url}"
                
                print(req_url)
                res = session.get(req_url)

                if res.status_code == 200:
                    if "error" in res.text.lower():
                        print(f"Error: error, please do not click the page frequently.")
                        time.sleep(5)
                        continue
                        
                    soup = BeautifulSoup(res.text, "html.parser")
                    rows = soup.find_all("tr")
                    pages = []

                    for row in rows:
                        tds = row.find_all('td')
                        if tds:
                            name = tds[0].get_text(strip=True)
                            method = tds[1].get_text(strip=True)
                            username = tds[2].get_text(strip=True)
                            password = tds[3].get_text(strip=True)
                            level = tds[4].get_text(strip=True)
                           
                            pages.append(f"{name}:{method}:{username}:{password}:{level}")

                    intel = IntelFactory.make({
                        "label": f"ChinaForumyWhack",
                        "source": f"{page_url}",
                        "pages": pages
                    })

                    intels.append(intel)
                    print(Messages["intel.progress"]({"intel": intel, "all": all_pages, "count": current_page}))

                    current_page += 1

                else:
                    if "error, please do not click the page frequently." in res.text.lower():
                        print(f"Error: error, please do not click the page frequently.")
                        time.sleep(5)
                    else:
                        print(f"Failed to access page {current_page}. Status code: {res.status_code}")
                        time.sleep(5)
                        
            except Exception as e:
                print(f"An error occurred: {e}")
                current_page -= 1
                time.sleep(5)  

        print(Messages["collector.collected"]({"intels": intels}))
        
        return intels
