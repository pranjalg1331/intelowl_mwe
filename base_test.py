# This is the base test class for all analyzers to run tests that are common among all

import unittest

class BaseAnalyzerTest(unittest.TestCase):
    analyzer_class = None  # To be set by subclasses
    
    def test_supported_types(self):
        if not self.analyzer_class:
            self.skipTest("No analyzer class specified")
        
        analyzer = self.analyzer_class()
        print(analyzer.name)
        for observable in analyzer.supported_types:
            result = analyzer.run(observable)
            self.assertIn(f"Analyzing {observable}", result)