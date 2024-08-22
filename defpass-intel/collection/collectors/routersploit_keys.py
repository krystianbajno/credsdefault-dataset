import json
from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class RouterSploitKeys(Collector):
    def run(self) -> List[Intel]:
        autourls = "https://github.com/threat9/routersploit/tree/master/routersploit/resources/ssh_keys"
        base_raw = "https://raw.githubusercontent.com"
        intels = []
        
        res = httpx.request("GET", autourls)
        print(Messages["collector.connected"](autourls))
                
        session = httpx.Client(base_url=base_raw)
        print(Messages["collector.connected"](base_raw))
        
        soup = BeautifulSoup(res.text, "html.parser")
        
        script_tag = soup.find("script", {"type": "application/json", "data-target": "react-app.embeddedData"})

        if script_tag:
            script_content = script_tag.string.strip()
            
            data = json.loads(script_content)
            
            items = data["payload"]["tree"]["items"]
            
            scrap_auto = []

            for item in items:
                if item["contentType"] == "file":
                    label = item["name"]
                    label = "AUTOSCRAP_" + label

                    url =  "/threat9/routersploit/master/" + item["path"]
                    scrap_auto.append((label, url))
                    
            all = len(scrap_auto)
            count = 0
            for label, href in scrap_auto:   
                res = session.get(href)
                                
                intel = IntelFactory.make({
                    "label": label,
                    "source": base_raw + href,
                    "pages": [res.text],
                })
                
                intels.append(intel)
                
                count = count + 1
                print(Messages["intel.progress"]({"intel": intel, "all": all, "count": count}))
        else:
            print("Script tag with the specified attributes was not found.")


        print(Messages["collector.collected"]({"intels": intels}))

        return intels