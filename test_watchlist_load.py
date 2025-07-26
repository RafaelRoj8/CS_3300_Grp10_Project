import unittest
from PriceSnipr import save_watchlist, load_watchlist

class TestWatchlistLoad(unittest.TestCase):
    def test_load_watchlist(self):
        test_watchlist = [
            {"title": "Test Product", "link": "http://example.com", "target": 100.00, "notified": False}
        ]
        test_history = [
            {"title": "Test Product", "price": "$95.00", "when": "2025-07-26 20:30"}
        ]
        save_watchlist(test_watchlist, test_history)
        items, history = load_watchlist()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Test Product")
        self.assertEqual(history[0]["price"], "$95.00")

if __name__ == "__main__":
    unittest.main()
