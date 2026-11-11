from collections.abc import Iterable, Mapping
from typing import Any


def calculate_total_revenue(
    sales: Iterable[Mapping[str, Any]],
) -> float:
    """Calculate revenue from records containing quantity and unit_price."""
    return round(
        sum(float(sale["quantity"]) * float(sale["unit_price"]) for sale in sales),
        2,
    )


def calculate_total_orders(sales: Iterable[Mapping[str, Any]]) -> int:
    """Count the number of sales records."""
    return sum(1 for _ in sales)


def calculate_unique_customers(sales: Iterable[Mapping[str, Any]]) -> int:
    """Count distinct customer IDs in sales records."""
    return len({sale["customer_id"] for sale in sales})
