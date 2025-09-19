from flask import Flask, request, jsonify
from app.database import db_session, init_db
from app.models import Product
from app.crud import create_product
from app.utils import timestamp_log
import time
import socket

app = Flask(__name__)
init_db()

@app.route("/products/create", methods=["POST"])
@timestamp_log
def create():
    data = request.get_json()
    hostname = socket.gethostname()
    try:
        product = create_product(data["name"], data["stock_quantity"], data["price"], data["description"])
        return jsonify({"status": "success", 
                        "id": product.id, 
                        "name": product.name, 
                        "stock":product.stock_quantity, 
                        "description":product.description, 
                        "replica":hostname}), 201
    except Exception as e:
        return jsonify({"status": "error", 
                        "message": str(e),
                        "replica":hostname}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "alive"}), 200

if __name__ == "__main__":
    app.run()
