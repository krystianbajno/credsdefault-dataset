import json
from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class SecLists(Collector):
    def __init__(self, base_url):
        self.base_url = base_url if base_url else "https://github.com"
        
    def __urls(self):
        return {
            ("MANUAL_SCADA", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/scada-pass.csv"),
            ("MANUAL_OracleEBS_passwords", '/danielmiessler/SecLists/master/Passwords/Default-Credentials/Oracle%20EBS%20passwordlist.txt'),
            ("MANUAL_OracleEBS_users", '/danielmiessler/SecLists/master/Passwords/Default-Credentials/Oracle%20EBS%20userlist.txt'),
            ("MANUAL_Avaya_passwords", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/avaya_defaultpasslist.txt"),
            ("MANUAL_CryptoMiners", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/cryptominers.txt"),
            ("MANUAL_DefaultBetter_passwords", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/db2-betterdefaultpasslist.txt"),
            ("MANUAL_DefaultPasswords_CSV", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/default-passwords.csv"),
            ("MANUAL_DefaultPasswords_TXT", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/default-passwords.txt"),
            ("MANUAL_FTP_BetterPasslist", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt"),
            ("MANUAL_MsSQL_BetterDefaultPassList", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/mssql-betterdefaultpasslist.txt"),
            ("MANUAL_MySQL_BetterDefaultPassList", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/mysql-betterdefaultpasslist.txt"),
            ("MANUAL_Oracle_BetterDefaultPasslist", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/oracle-betterdefaultpasslist.txt"),
            ("MANUAL_PostgreSQL_BetterDefaultPassList", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/postgres-betterdefaultpasslist.txt"),
            ("MANUAL_SSH_Better_passwords", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/ssh-betterdefaultpasslist.txt"),
            ("MANUAL_Telnet_BetterDefaultPasslist", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/telnet-betterdefaultpasslist.txt"),
            ("MANUAL_Telnet_PhenoElit", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/telnet-phenoelit.txt"),
            ("MANUAL_Tomcat_BetterDefaultPasslist", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/tomcat-betterdefaultpasslist.txt"),
            ("MANUAL_VNC_BetterDefaultPasslist", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/vnc-betterdefaultpasslist.txt"),
            ("MANUAL_Windows_BetterDefaultPasslist", "/danielmiessler/SecLists/master/Passwords/Default-Credentials/windows-betterdefaultpasslist.txt"),
            ("MANUAL_SAP_DefaultUsernames", "/danielmiessler/SecLists/master/Usernames/sap-default-usernames.txt")
        }
        
    def __autourls(self):
        return "/danielmiessler/SecLists/tree/master/Passwords/Default-Credentials/Routers"
    
    def run(self) -> List[Intel]:
        autourls = self.base_url + self.__autourls()
        base_raw = "https://raw.githubusercontent.com"
        intels = []
        res = httpx.request("GET", autourls)
        print(Messages["collector.connected"](self.base_url))
                
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
                    label = label.replace("default-", "")
                    label = label.replace("default_", "")
                    label = label.replace("-", "-")
                    label = "AUTOSCRAP_" + label

                    url =  "/danielmiessler/SecLists/master/" + item["path"]
                    scrap_auto.append((label, url))

            all = len(scrap_auto)
            count = 0
            for label, href in scrap_auto:   
                res = session.get(href)
                
                pages = res.text.split("\n")
                
                intel = IntelFactory.make({
                    "label": label,
                    "source": self.base_url + href,
                    "pages": pages,
                })
                
                intels.append(intel)
                
                count = count + 1
                print(Messages["intel.progress"]({"intel": intel, "all": all, "count": count}))

        else:
            print("Script tag with the specified attributes was not found.")


        manual_urls = self.__urls()
        all = len(scrap_auto)
        count = 0
        for label, href in manual_urls:   
            res = session.get(href)
            
            pages = res.text.split("\n")
            
            intel = IntelFactory.make({
                "label": label,
                "source": self.base_url + href,
                "pages": pages,
            })
            
            intels.append(intel)
            
            count = count + 1
            print(Messages["intel.progress"]({"intel": intel, "all": all, "count": count}))
        
        
        print(Messages["collector.collected"]({"intels": intels}))
        return intels