import unittest
from unittest.mock import patch

from app import create_app


class DashboardTests(unittest.TestCase):
    def test_index_displays_metrics_from_sql_sales(self):
        sales = [
            {"customer_id": 1, "quantity": 2, "unit_price": 12.5},
            {"customer_id": 2, "quantity": 1, "unit_price": 7.25},
        ]
        with patch("src.routes.dashboard.fetch_sales", return_value=sales):
            response = create_app().test_client().get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"$32.25", response.data)
        self.assertEqual(response.data.count(b'<p class="metric-value">2</p>'), 2)


if __name__ == "__main__":
    unittest.main()
