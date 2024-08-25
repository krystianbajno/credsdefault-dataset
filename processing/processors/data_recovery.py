from typing import List, Optional
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory
from bs4 import BeautifulSoup

class DataRecovery(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        for intel in intels:
            for page in intel.pages:
                soup = BeautifulSoup(page, "html.parser")
                
                rows = soup.find_all('tr')

                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) >= 7: 
                        manufacturer = cols[0].text.strip()
                        model = cols[1].text.strip()
                        version = cols[2].text.strip() if len(cols) > 2 else None
                        method = cols[3].text.strip() if len(cols) > 3 else None
                        login = cols[4].text.strip() if len(cols) > 4 else None
                        password = cols[5].text.strip() if len(cols) > 5 else None
                        role = cols[6].text.strip() if len(cols) > 6 else None
                        comment = cols[7].text.strip() if len(cols) > 7 else None

                        credential_data = {
                            "manufacturer": manufacturer,
                            "model": model,
                            "version": version,
                            "login": login,
                            "role": role,
                            "password": password,
                            "source": intel.label,
                            "method": method,
                            "comment": comment,
                            "port": None 
                        }
                        
                        credential = CredentialsFactory.make(credential_data)
                        credentials.append(credential)

            
        return credentials
