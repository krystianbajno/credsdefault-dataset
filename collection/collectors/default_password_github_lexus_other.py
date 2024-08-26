# https://github.com/Lexus89/default-passwords/blob/master/routerpasswords_portforward.csv
# https://github.com/Lexus89/default-passwords/blob/master/default-passwords_other.csv

from typing import List
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages

class DefaultPasswordGithubLexusOther(Collector):
    def run(self) -> List[Intel]:
        label = "DefaultPasswordGithubLexusOther"
        intels = []
        
        url = "https://raw.githubusercontent.com/Lexus89/default-passwords/master/default-passwords_other.csv"
        res = httpx.request("GET", url)
        print(Messages["collector.connected"](url))

        def parse_line(line: str) -> List[str]:
            parts = line.split(",")

            i = 0
            while i < len(parts) - 1:
                if parts[i].strip().endswith("Inc.") or parts[i].strip().endswith("Ltd."):
                    parts[i] = parts[i] + "," + parts[i + 1]
                    del parts[i + 1]
                else:
                    i += 1
            return parts

        lines = res.text.strip().split("\n")[1:] 
        pages = []

        for line in lines:
            parsed_line = parse_line(line)
            pages.append(parsed_line)

        intel = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": pages,
        })
        
        intels.append(intel)
        
        return intels
