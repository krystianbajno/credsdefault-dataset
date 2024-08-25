from typing import List
from bs4 import BeautifulSoup
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory

class DefPass(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        
        for intel in intels:
            for page in intel.pages:
                soup = BeautifulSoup(page, "html.parser")

                vendor = self.extract_field(soup, "Vendor:")
                device = self.extract_field(soup, "Device:")
                default_password = self.extract_field(soup, "Default password:")
                port = self.extract_field(soup, "Port:")
                protocol = self.extract_field(soup, "Protocol:")

                credential_data = {
                    "manufacturer": vendor,
                    "model": device,
                    "password": default_password,
                    "port": port,
                    "method": protocol,
                    "source": intel.source,
                }

                credential = CredentialsFactory.make(credential_data)
                credentials.append(credential)

        return credentials

    def extract_field(self, soup: BeautifulSoup, field_name: str) -> str:
        field = soup.find(text=field_name)
        if field:
            return field.find_next(string=True).strip()
        return None

    def extract_source(self, soup: BeautifulSoup) -> str:
        field = soup.find(text="Source:")
        if field:
            link_tag = field.find_next('a')
            if link_tag and link_tag.has_attr('href'):
                return link_tag['href']
        return None
