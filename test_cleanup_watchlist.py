import unittest
from PriceSnipr import save_watchlist, load_watchlist

class TestCleanupWatchlist(unittest.TestCase):
    def test_removed_item_does_not_remain(self):
        items = [
            {"title": "A", "link": "urlA", "target": 50.0, "notified": False},
            {"title": "B", "link": "urlB", "target": 100.0, "notified": True}
        ]
        history = []
        save_watchlist(items, history)

        # Simulate removing item B
        items = [item for item in items if item["title"] != "B"]
        save_watchlist(items, history)
        loaded_items, _ = load_watchlist()

        titles = [item["title"] for item in loaded_items]
        self.assertNotIn("B", titles)
        self.assertIn("A", titles)

if __name__ == "__main__":
    unittest.main()
