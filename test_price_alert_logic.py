import unittest
from PriceSnipr import notification

class TestPriceAlertLogic(unittest.TestCase):
    def test_desktop_notification_mock(self):
        # This is just to show that notification call works — actual OS notification won't be tested
        try:
            notification.notify(
                title="Test Alert",
                message="Test message",
                timeout=3
            )
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()


