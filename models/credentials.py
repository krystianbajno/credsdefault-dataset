
class Credentials:
    def __init__(self, 
        model: str = None, 
        manufacturer: str = None, 
        version: str = None, 
        role: str = None, 
        login: str = None,
        password: str = None,
        method: str = None,
        source: str = None,
        comment: str = None,
        port: str = None,
        address: str = None
    ):
        self.manufacturer = manufacturer
        self.model = model
        self.version = version
        self.role = role
        self.login = login
        self.password = password
        self.method = method
        self.source = source
        self.comment = comment
        self.port = port
        self.address = address
        
    def set_manufacturer(self, manufacturer: str) -> None: 
        self.manufacturer = manufacturer
    
    def set_role(self, role: str) -> None:
        self.role = role
    
    def set_method(self, method: str) -> None:
        self.method = method
        
    def set_version(self, version: str) -> None:
        self.version = version
        
    def set_login(self, login: str) -> None:
        self.login = login
        
    def set_password(self, password: str) -> None:
        self.password = password
        
    def set_model(self, model: str) -> None:
        self.model = model
        
    def set_source(self, source: str) -> None:
        self.source = source
        
    def set_comment(self, comment: str) -> None:
        self.comment = comment
        
    def set_port(self, port: str) -> None:
        self.port = port
        
    def set_address(self, address: str) -> None:
        self.address = address
        
    def to_dict(self) -> dict:
        return {
            "manufacturer": self.manufacturer,
            "model": self.model,
            "version": self.version,
            "role": self.role,
            "login": self.login,
            "password": self.password,
            "method": self.method,
            "source": self.source,
            "comment": self.comment,
            "port": self.port,
            "address": self.address
        }