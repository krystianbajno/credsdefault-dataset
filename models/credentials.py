
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
        
    def set_manufacturer(self, manufacturer: str): 
        self.manufacturer = manufacturer
    
    def set_role(self, role: str) -> None:
        self.role = role
    
    def set_method(self, method):
        self.method = method
        
    def set_version(self, version):
        self.version = version
        
    def set_login(self, login):
        self.login = login
        
    def set_password(self, password):
        self.password = password
        
    def set_model(self, model):
        self.model = model
        
    def set_source(self, source):
        self.source = source
        
    def set_comment(self, comment):
        self.comment = comment
        
    def set_port(self, port):
        self.port = port
        
    def set_address(self, address):
        self.address = address