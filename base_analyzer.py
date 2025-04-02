class BaseAnalyzer:
    def __init__(self, name, supported_types):
        self.name = name
        self.supported_types = supported_types

    def run(self, observable_type, data):
        if observable_type not in self.supported_types:
            raise ValueError(f"Unsupported observable type: {observable_type}")
        return f"{self.name} analyzed {data} as {observable_type}"