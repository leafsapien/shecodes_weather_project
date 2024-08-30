import unittest
from tests.test_convert_f_to_c import ConvertTempTests #1
from tests.test_convert_date import ConvertDateTests #2
from tests.test_calculate_mean import CalculateMeanTests #4
from tests.test_load_data_from_csv import LoadCSVTests #5
from tests.test_find_min import FindMinTests #6
from tests.test_find_max import FindMaxTests #7
from tests.test_generate_summary import GenerateSummaryTests #8
from tests.test_generate_daily_summary import GenerateDailySummaryTests #9

runner = unittest.TextTestRunner()

print("Running Tests...\n")
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(ConvertTempTests)))) #1
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(ConvertDateTests)))) #2
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(CalculateMeanTests)))) #4
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(LoadCSVTests)))) #5
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(FindMinTests)))) #6
runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(FindMaxTests)))) #7
# runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(GenerateSummaryTests)))) #8
# runner.run(unittest.TestSuite((unittest.TestLoader().loadTestsFromTestCase(GenerateDailySummaryTests)))) #9
