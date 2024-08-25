from typing import List
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory

from bs4 import BeautifulSoup

class CirtNet(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        for intel in intels:
            for page in intel.pages:
                soup = BeautifulSoup(page, "html.parser")
                
                user_id_tag = soup.find('td', text='User ID')
                user_id = user_id_tag.find_next_sibling('td').text.strip() if user_id_tag else None

                password_tag = soup.find('td', text='Password')
                password = password_tag.find_next_sibling('td').text.strip() if password_tag else None

                method_tag = soup.find('td', text='Method')
                method = method_tag.find_next_sibling('td').text.strip() if method_tag else None

                level_tag = soup.find('td', text='Level')
                level = level_tag.find_next_sibling('td').text.strip() if level_tag else None
                
                notes_tag = soup.find('td', text='Notes')
                notes = notes_tag.find_next_sibling('td').text.strip() if notes_tag else None
                
                version_tag = soup.find('td', text='Version')
                version = version_tag.find_next_sibling('td').text.strip() if version_tag else None
              
                credential = CredentialsFactory.make({
                    "manufacturer": intel.label,
                    "login": user_id,
                    "password": password,
                    "role": level,
                    "comment": notes,
                    "version": version,
                    "method": method,
                    "source": intel.source                
                })
                
                credentials.append(credential)
                    
        return credentials
