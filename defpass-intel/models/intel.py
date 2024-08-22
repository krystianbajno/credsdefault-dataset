from typing import List


class Intel:
    def __init__(self, label: str = None, pages: List[str] = None, source: str = None):
        self.label = label
        self.pages = pages
        self.source = source
        
    def set_label(self, label):
        self.label = label
    
    def set_pages(self, pages):
        self.pages = pages
        
    def set_source(self, source):
        self.source = source
        
    def to_dict(self):
        return {
            "label": self.label,
            "pages": self.pages,
            "source": self.source
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            label=data.get("label"),
            pages=data.get("pages"),
            source=data.get("source")
        )
