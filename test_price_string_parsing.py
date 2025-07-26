import unittest

class TestPriceStringParsing(unittest.TestCase):
    def test_convert_price_string_to_float(self):
        def parse_price(s):
            try:
                return float(s.replace("$", "").replace(",", ""))
            except:
                return None

        self.assertEqual(parse_price("$1,234.56"), 1234.56)
        self.assertEqual(parse_price("$0.99"), 0.99)
        self.assertEqual(parse_price("Free"), None)

if __name__ == "__main__":
    unittest.main()

