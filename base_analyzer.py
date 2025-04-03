#This class is a mock version of analyzer base class

class BaseAnalyzer:
    def __init__(self, name, supported_types):
        self.name = name
        self.supported_types = supported_types
    
    def run(self, observable_type):
        if observable_type not in self.supported_types:
            raise ValueError(f"{self.name} does not support {observable_type}")
        return f"Analyzing {observable_type} with {self.name}"