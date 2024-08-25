from typing import List, Optional
from bs4 import BeautifulSoup
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory, CredentialsDict, CredentialsEnum

class PasswordsDatabase(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []

        for intel in intels:
            for page in intel.pages:
                soup = BeautifulSoup(page, "html.parser")

                tables = soup.find_all('tr')

                for i in range(0, len(tables), 2):
                    try:
                        details = tables[i + 1].find_all('p')

                        product = self.extract_text(details, 0, 'Product:')
                        version = self.extract_text(details, 1, 'Version:')
                        method = self.extract_text(details, 2, 'Method:')
                        user_id = self.extract_text(details, 3, 'User ID:')
                        password = self.extract_text(details, 4, 'Password:')

                        credential_data: CredentialsDict = {
                            "manufacturer": intel.label,  
                            "model": product,
                            "version": version,
                            "login": user_id,
                            "password": password,
                            "source": intel.source,
                            "method": method
                        }

                        credential = CredentialsFactory.make(credential_data)
                        credentials.append(credential)
                        
                    except Exception as e:
                      pass
                

        return credentials

    @staticmethod
    def extract_text(details: List, index: int, prefix: str) -> Optional[str]:
        if len(details) > index:
            return details[index].text.replace(prefix, '').strip()
        return None
