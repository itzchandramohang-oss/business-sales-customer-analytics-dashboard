import unittest

from src.analysis.metrics import (
    calculate_total_orders,
    calculate_total_revenue,
    calculate_unique_customers,
)


class MetricsTests(unittest.TestCase):
    def setUp(self):
        self.sales = [
            {"customer_id": 1, "quantity": 2, "unit_price": 12.5},
            {"customer_id": 2, "quantity": 1, "unit_price": 7.25},
            {"customer_id": 1, "quantity": 3, "unit_price": 4.0},
        ]

    def test_calculate_total_revenue(self):
        self.assertEqual(calculate_total_revenue(self.sales), 44.25)

    def test_calculate_total_orders(self):
        self.assertEqual(calculate_total_orders(self.sales), 3)

    def test_calculate_unique_customers(self):
        self.assertEqual(calculate_unique_customers(self.sales), 2)


if __name__ == "__main__":
    unittest.main()
