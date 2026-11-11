from flask import Flask

from src.config import Config
from src.db.sync import sync_sales_to_mongo
from src.routes.dashboard import dashboard_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(dashboard_bp)
    return app


app = create_app()


@app.cli.command("sync-sales")
def sync_sales_command() -> None:
    """Copy SQL sales into MongoDB orders."""
    synced_count = sync_sales_to_mongo()
    print(f"Synchronized {synced_count} sales to MongoDB.")


if __name__ == "__main__":
    app.run(debug=app.config.get("DEBUG", False))
