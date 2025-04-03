# This is an example analyzer inheriting the base analyzer class

from base_analyzer import BaseAnalyzer

class ExampleAnalyzer(BaseAnalyzer):
    def __init__(self):
        super().__init__("ExampleAnalyzer", ["IP", "DOMAI"])
    
    def run(self, observable_type):
        return super().run(observable_type) + " - Example Specific Logic"