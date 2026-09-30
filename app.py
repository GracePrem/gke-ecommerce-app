from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 54999,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 24999,
        "category": "Mobiles"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2999,
        "category": "Electronics"
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 4999,
        "category": "Wearables"
    }
]


@app.route("/")
def home():
    return "E-Commerce Backend API is running"


@app.route("/api/products")
def get_products():
    return jsonify(products)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
