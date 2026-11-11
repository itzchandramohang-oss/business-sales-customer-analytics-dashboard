from flask import Blueprint, render_template

from src.analysis.metrics import (
    calculate_total_orders,
    calculate_total_revenue,
    calculate_unique_customers,
)
from src.db.sql_client import fetch_sales

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.get("/")
def index():
    sales = fetch_sales()
    return render_template(
        "index.html",
        metrics={
            "total_revenue": calculate_total_revenue(sales),
            "total_orders": calculate_total_orders(sales),
            "unique_customers": calculate_unique_customers(sales),
        },
    )
