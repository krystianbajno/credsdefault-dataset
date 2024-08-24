from collection.collector import Collector
from factory.intel_factory import IntelFactory
from collection.collectors.data.custom import data

class Custom(Collector):
    def run(self):
        intels = []
        
        for entry in data:
            intels.append(
                IntelFactory.make(entry)
            )
       
        return intels