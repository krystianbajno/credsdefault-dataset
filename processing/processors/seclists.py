from typing import List
from processing.processor import Processor
from models.credentials import Credentials
from models.intel import Intel
from factory.credentials_factory import CredentialsFactory

class SecLists(Processor):
    def process(self, intels: List[Intel]) -> List[Credentials]:
        credentials: List[Credentials] = []

        for intel in intels:
            handler = self.processing_table().get(intel.label)

            if handler:
                credentials.extend(handler(intel))
            elif "AUTOSCRAP" in intel.label:
                credentials.extend(self.process_autoscrap(intel))
            else:
                print(f"Unhandled Intel Label: {intel.label}")
                print(intel.pages)

        return credentials

    def processing_table(self):
        return {
            "AUTOSCRAP_0ALL-USERNAMES-AND-PASSWORDS.txt": self.process_allusernames_passwords,
            "MANUAL_DefaultPasswords_CSV": self.process_manual_default_passwords_csv,
            "MANUAL_DefaultPasswords_TXT": self.process_manual_default_passwords_txt,
            "MANUAL_MsSQL_BetterDefaultPassList": self.process_simple_list,
            "MANUAL_OracleEBS_passwords": self.process_simple_list,
            "MANUAL_DefaultBetter_passwords": self.process_simple_list,
            "MANUAL_SSH_Better_passwords": self.process_simple_list,
            "MANUAL_CryptoMiners": self.process_simple_list,
            "MANUAL_Telnet_BetterDefaultPasslist": self.process_simple_list,
            "MANUAL_Tomcat_BetterDefaultPasslist": self.process_simple_list,
            "MANUAL_SAP_DefaultUsernames": self.process_simple_list,
            "MANUAL_SCADA": self.process_scada_list,
            "MANUAL_MySQL_BetterDefaultPassList": self.process_simple_list,
            "MANUAL_PostgreSQL_BetterDefaultPassList": self.process_simple_list,
            "MANUAL_VNC_BetterDefaultPasslist": self.process_simple_list,
            "MANUAL_OracleEBS_users": self.process_simple_list,
            "MANUAL_Telnet_PhenoElit": self.process_simple_list,
            "MANUAL_FTP_BetterPasslist": self.process_simple_list,
            "MANUAL_Windows_BetterDefaultPasslist": self.process_simple_list,
            "MANUAL_Oracle_BetterDefaultPasslist": self.process_simple_list,
            "MANUAL_Avaya_passwords": self.process_simple_list
        }

    def process_allusernames_passwords(self, intel: Intel) -> List[Credentials]:
        return [
            CredentialsFactory.make({
                "manufacturer": "generic",
                "login": page,
                "password": page,
                "comment": "This is a password or username"
            }) for page in intel.pages
        ]

    def process_autoscrap(self, intel: Intel) -> List[Credentials]:
        credentials = []
        manufacturer = intel.label.split("_")[1]

        if "users" in intel.label:
            credentials.extend(
                CredentialsFactory.make({
                    "login": page,
                    "manufacturer": manufacturer
                }) for page in intel.pages
            )

        if "passwords" in intel.label:
            credentials.extend(
                CredentialsFactory.make({
                    "password": page,
                    "manufacturer": manufacturer
                }) for page in intel.pages
            )

        return credentials

    def process_manual_default_passwords_txt(self, intel: Intel) -> List[Credentials]:
        return [
            CredentialsFactory.make({
                "password": page,
                "manufacturer": "generic"
            }) for page in intel.pages
        ]

    def process_manual_default_passwords_csv(self, intel: Intel) -> List[Credentials]:
        credentials = []

        for page in intel.pages:
            data = page.split(",")
            if len(data) >= 4:
                credentials.append(
                    CredentialsFactory.make({
                        "manufacturer": data[0],
                        "login": data[1],
                        "password": data[2],
                        "comment": data[3]
                    })
                )

        return credentials

    def process_simple_list(self, intel: Intel) -> List[Credentials]:
        credentials = []
        for page in intel.pages:
            if ":" in page:
                login, password = page.split(":", 1)
                credentials.append(
                    CredentialsFactory.make({
                        "login": login,
                        "password": password,
                        "manufacturer": intel.label.split("_")[1].lower()
                    })
                )
        return credentials

    def process_scada_list(self, intel: Intel) -> List[Credentials]:
        credentials = []
        for page in intel.pages:
            if "," in page:
                parts = page.split(",", 2)
                if len(parts) >= 3:
                    manufacturer, device, login_password = parts[:3]
                    if ":" in login_password:
                        login, password = login_password.split(":", 1)
                        credentials.append(
                            CredentialsFactory.make({
                                "manufacturer": manufacturer.strip(),
                                "login": login.strip(),
                                "password": password.strip(),
                                "comment": f"Device: {device.strip()}"
                            })
                        )
        return credentials
