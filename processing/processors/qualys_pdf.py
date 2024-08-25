from typing import List
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory, CredentialsDict, CredentialsEnum

class QualysPDF(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []

        for intel in intels:
            for page in intel.pages:
                content = page.strip()
                lines = content.splitlines()

                manufacturer = None
                model = None
                service_protocol = None
                username = None
                password = None

                for line in lines:
                    if "QID" in line:
                        if "Default Credentials" in line:
                            manufacturer_model = line.split("–")[1].split("Default Credentials")[0].strip()
                            
                            if " " in manufacturer_model:
                                manufacturer, model = manufacturer_model.rsplit(" ", 1)
                            else:
                                manufacturer = manufacturer_model
                                model = None

                        else:
                            manufacturer = model = None

                    elif "Service/Protocol" in line:
                        service_protocol = username = password = None
                    elif any(proto in line for proto in ["HTTP service", "FTP", "TELNET", "Postgres DB", "SSH/TELNET"]):
                        parts = line.split()
                        if len(parts) >= 4:
                            service_protocol = parts[0]
                            username = parts[2]
                            password = parts[3]

                            if manufacturer is None and model is None:
                                manufacturer = "Generic"
                                model = service_protocol

                            if service_protocol and username and password:
                                credential_data: CredentialsDict = {
                                    "manufacturer": manufacturer,
                                    "model": model,
                                    "version": None,
                                    "login": username,
                                    "password": password,
                                    "source": intel.label or CredentialsEnum.NO_DATA.value,
                                    "method": service_protocol,
                                }

                                credential = CredentialsFactory.make(credential_data)
                                credentials.append(credential)

                        else:
                            pass

        return credentials
