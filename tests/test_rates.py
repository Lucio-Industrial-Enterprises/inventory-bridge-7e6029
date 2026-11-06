import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # --- standard service (preserved) ---

    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit(self):
        self.assertEqual(shipping_quote(2, "local", "standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", "standard"), 11.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    # --- express service ---

    def test_express_local(self):
        # express = standard base + $7 surcharge
        self.assertEqual(shipping_quote(2, "local", "express"), 15.0)

    def test_express_regional(self):
        self.assertEqual(shipping_quote(2, "regional", "express"), 18.0)

    def test_express_fractional_weight(self):
        # 1.5 * 1.5 kg + 5.0 base + 7.0 surcharge = 14.25
        self.assertEqual(shipping_quote(1.5, "local", "express"), 14.25)

    def test_express_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local", "express")

    # --- validation ---

    def test_unknown_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "intergalactic")

    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", "overnight")
