import httpx
import string
from collection.collector import Collector
from bs4 import BeautifulSoup
from factory.intel_factory import IntelFactory
from cli.messages import Messages

# https://defpass.com/index.php
"""
Summary
URL: https://defpass.com/index.php
Status: 200
Source: Network
Address: 213.190.30.57:443

Request
:method: POST
:scheme: https
:authority: defpass.com
:path: /index.php
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9
Connection: keep-alive
Content-Length: 10
Content-Type: application/x-www-form-urlencoded
Host: defpass.com
Origin: https://defpass.com
Referer: https://defpass.com/index.php
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15

Response
:status: 200
Content-Encoding: gzip
Content-Length: 2382
Content-Type: text/html; charset=UTF-8
Date: Fri, 23 Aug 2024 16:03:22 GMT
Server: nginx
Vary: Accept-Encoding
x-powered-by: PHP/7.4.33, PleskLin

Request Data
MIME Type: application/x-www-form-urlencoded
query: asus
"""

# get a list of iot manufacturers

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

            

