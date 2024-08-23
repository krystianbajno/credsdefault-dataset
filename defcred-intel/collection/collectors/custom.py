

from collection.collector import Collector
from factory.intel_factory import IntelFactory

data = [
    {
      "label": "netgear",
      "pages": [
          "NETGEAR:all:admin:password:",
          "NETGEAR:old:admin:1234",
          "NETGEAR:ReadyNAS OS::password:",
          "NETGEAR:ReaddyDATA OS::password:",
          "NETGEAR:RAIDiator::netgear1",
          "NETGEAR:Infrant::infrant1",
          "NETGEAR:Switches:admin:::"
        ],
      "source": "https://kb.netgear.com/1148/What-are-the-default-user-interface-passwords-for-NETGEAR-devices"
    },
    {
        "label": "Nessus",
        "pages": [
            ":Nessus Pro:wizard:admin:"
        ],
        "source": "custom"
    },
    {
        "label": "Oracle",
        "pages": [
            "Oracle::oracle:oracle:",
            "Oracle::sys:oracle:",
            "Oracle::HR:oracle:",
            "Oracle::system:oracle:"
        ],
        "source": "custom"
    },
    {
        "label": "Nintex",
        "pages": [
            "Nintex:Kryon RPA:AuthAdmin:Kryon123:administrator",
            "Nintex:Kryon RPA:TestUser:Kryon123!:testuser",
        ],
        "source": "custom"
    },
    {
        "label": "Holm Security",
        "pages": [
            "Holm Security:OnPrem:admin:holmsecurity:",
        ],
        "source": "custom"
    },
    {
        "label": "PfSense",
        "pages": [
            "PfSense::admin:pfsense:",
        ],
        "source": "custom"
    },
    {
        "label": "Huawei",
        "pages": [
            "Huawei::Administrator:Admin@9000"
        ],
        "source": "custom"
    },
    {
        "label": "Stellar Cyber",
        "pages": [
            "Stellar Cyber:User Interface:admin:changeme:",
            "Stellar Cyber:Sensor CLI:aella:changeme:",
            "Stellar Cyber:DP Appliance CLI:stellar:stellar:"
        ],
        "source": "custom"
    }
]

class Custom(Collector):
    def run(self):
        intels = []
        
        for entry in data:
            intels.append(
                IntelFactory.make(entry)
            )
       
        return intels