import unittest
from datetime import datetime

from src.db.sync import build_order_document


class SyncTests(unittest.TestCase):
    def test_build_order_document_maps_sql_sale(self):
        sale_date = datetime(2026, 1, 15, 10, 30)
        sale = {
            "sale_id": 12,
            "customer_id": 3,
            "customer_name": "Example customer",
            "product_id": 7,
            "product_name": "Example product",
            "product_category": "Accessories",
            "quantity": 2,
            "unit_price": 24.99,
            "sale_date": sale_date,
        }

        self.assertEqual(
            build_order_document(sale),
            {
                "_id": "sql-sale-12",
                "sale_id": 12,
                "source": "sql_sales",
                "customer_id": 3,
                "customer_name": "Example customer",
                "order_date": sale_date,
                "items": [
                    {
                        "product_id": 7,
                        "name": "Example product",
                        "category": "Accessories",
                        "quantity": 2,
                        "unit_price": 24.99,
                    }
                ],
                "status": "completed",
            },
        )


if __name__ == "__main__":
    unittest.main()
