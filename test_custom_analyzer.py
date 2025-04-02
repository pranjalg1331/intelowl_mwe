from example_analyzer import ExampleAnalyzer
from base_test import BaseAnalyzerTest


class TestExampleAnalyzer(BaseAnalyzerTest):
    analyzer_class = ExampleAnalyzer  # Specifies which analyzer to test
    
    def test_custom(self):
        analyzer = self.analyzer_class()
        self.assertEqual(analyzer.run("IP"), "Analyzing IP with ExampleAnalyzer - Example Specific Logic")