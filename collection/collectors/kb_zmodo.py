# https://kb.zmodo.com/index.php?action=artikel&cat=1&id=12&artlang=en

import json
from typing import List
from bs4 import BeautifulSoup
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class KbZmodo(Collector):
    def run(self) -> List[Intel]:
        base_raw = "https://kb.zmodo.com/index.php?action=artikel&cat=1&id=12&artlang=en"
        
        res = httpx.get(base_raw, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"})
        print(Messages["collector.connected"](base_raw))
                
        soup = BeautifulSoup(res.text, "html.parser")    

        pages = []

        images = soup.find_all('img')

        for img in images:
            p_tag = img.find_next('p')
            
            if p_tag:
                title = p_tag.get_text(strip=True)
                
                login_blockquote = p_tag.find_next('blockquote')
                password_blockquote = login_blockquote.find_next_sibling('blockquote') if login_blockquote else None
                
                login = login_blockquote.get_text(strip=True) if login_blockquote else None
                password = password_blockquote.get_text(strip=True) if password_blockquote else None
                
                if login and not password:
                    if "Password:" in login:
                        login, password = login.split("Password:", 1)
                        login = login.replace("Login:", "").strip()
                        password = password.strip()
                else:
                    login = login.replace("Login:", "").strip() if login else None
                    password = password.replace("Password:", "").strip() if password else None
                
                if title and login and password:
                    pages.append(f"Zmodo:{title}:{login}:{password}")


        intel = IntelFactory.make({
            "label": "KbZmodo",
            "source": base_raw,
            "pages": pages,
        })
      
        intels = [intel]
        
        print(Messages["collector.collected"]({"intels": intels}))

        return intels
    
    