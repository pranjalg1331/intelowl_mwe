from base_test import BaseAnalyzerTestCase
from base_analyzer import BaseAnalyzer

class TestCustomAnalyzer(BaseAnalyzerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.analyzers.append(BaseAnalyzer("Custom Analyzer", ["domain", "ip"]))

    def test_invalid_observable(self):
        custom_analyzer = BaseAnalyzer("Custom Analyzer", ["domain", "ip"])
        with self.assertRaises(ValueError):
            custom_analyzer.run("hash", "abcd1234")