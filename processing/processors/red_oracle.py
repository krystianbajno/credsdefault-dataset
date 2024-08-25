from typing import List
from bs4 import BeautifulSoup
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory, CredentialsDict, CredentialsEnum

class RedOracle(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []
        
        for intel in intels:
            for page in intel.pages:
                soup = BeautifulSoup(page, "html.parser")

                vendor = self.extract_text(soup.find('h1', id="vendor-2wire"), "Vendor: ")
                model = self.extract_text(soup.find('h2', id="factory-default-settings-for-the-product-wifi-routers"), "Factory Default Settings for the product: ")

                extracted_data = {
                    "version": CredentialsEnum.NO_DATA.value,
                    "method": CredentialsEnum.NO_DATA.value,
                    "role": CredentialsEnum.NO_DATA.value,
                    "login": CredentialsEnum.NO_DATA.value,
                    "password": CredentialsEnum.NO_DATA.value,
                }

                keywords_map = {
                    "Version:": "version",
                    "Method:": "method",
                    "Level:": "role",
                    "Username:": "login",
                    "Password:": "password"
                }

                for detail in soup.find_all('li'):
                    text = detail.get_text(strip=True)
                    for keyword, key in keywords_map.items():
                        if keyword in text:
                            extracted_data[key] = text.replace(keyword, "").strip()

                credential_data: CredentialsDict = {
                    "manufacturer": vendor,
                    "model": model,
                    "version": extracted_data["version"],
                    "login": extracted_data["login"],
                    "role": extracted_data["role"],
                    "password": extracted_data["password"],
                    "source": intel.label,
                    "method": extracted_data["method"],
                }

                credentials.append(CredentialsFactory.make(credential_data))

        return credentials

    @staticmethod
    def extract_text(tag, prefix=""):
        return tag.text.replace(prefix, "").strip() if tag else CredentialsEnum.NO_DATA.value
