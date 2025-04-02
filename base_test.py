import unittest
from base_analyzer import BaseAnalyzer

class BaseAnalyzerTestCase(unittest.TestCase):
    analyzers = []

    @classmethod
    def setUpClass(cls):
        cls.analyzers = [
            BaseAnalyzer("DNS Analyzer", ["domain"]),
            BaseAnalyzer("IP Analyzer", ["ip"]),
            BaseAnalyzer("Hash Analyzer", ["hash"]),
        ]

    def supported_observables(self):
        test_data = {"domain": "example.com", "ip": "8.8.8.8", "hash": "abcd1234"}
        
        for analyzer in self.analyzers:
            for obs_type in analyzer.supported_types:
                result = analyzer.run(obs_type, test_data[obs_type])
                self.assertIn(obs_type, result)