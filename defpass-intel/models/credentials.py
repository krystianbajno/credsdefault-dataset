
class Credentials:
    def __init__(self, model: str, manufacturer: str, version: str, role: str, login: str, password: str, method, source):
        self.manufacturer = manufacturer
        self.model = model
        self.version = version
        self.role = role
        self.login = login
        self.password = password
        self.method = method
        self.source = source
        
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
        
    