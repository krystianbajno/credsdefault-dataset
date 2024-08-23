# https://cdn2.qualys.com/docs/qualys-vm-scanning-default-credentials.pdf

from typing import List
import httpx
from collection.collector import Collector
from models.intel import Intel
from factory.intel_factory import IntelFactory
from cli.messages import Messages
import PyPDF2
from io import BytesIO


class QualysPDF(Collector):
    def run(self) -> List[Intel]:
        url = "https://cdn2.qualys.com/docs/qualys-vm-scanning-default-credentials.pdf"
        label = "QualysPDF"
        res = httpx.request("GET", url)
        intels = []

        print(Messages["collector.connected"](url))
     
        pdf_file = BytesIO(res.content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        pdf_text = ""
        for page in range(len(pdf_reader.pages)):
            pdf_text += pdf_reader.pages[page].extract_text()
            
        pages = []
        for page in pdf_text.split("\n \n"):
            if "Copyright 2024 by Qualys, Inc. All Rights Reserved." in page:
                continue
            
            if "Qualys provides a scan option that allows users to perform password brute forcing attempts at scan time. " in page:
                continue
            
            if "Below is a list of QIDs that perform credential checks based on the password brute forcing option" in page:
                continue
            
            if "The Qualys Vulnerability KnowledgeBase provides many QIDs that can be scanned to determine" in page:
                continue
            
            if "Last updated: July  01, 202 4 " in page:
                continue
            
            pages.append(page)
            print(page)

            print("BREAK  \n\n\n\n")
            
            
        intel = IntelFactory.make({
            "label": label,
            "source": url,
            "pages": pages,
        })
                
        intels.append(intel)
            
        print(Messages["intel.progress"]({"intel": intel, "all": 1, "count": 1}))

        print(Messages["collector.collected"]({"intels": intels}))

        return intels