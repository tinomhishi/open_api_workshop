import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS

import jwt

SECRET_KEY = "your_secret_key"

app = Flask(__name__)

CORS(app)

USERS = {"user1": "password123", "admin": "securepassword"}

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 1200.50, "in_stock": True},
    {"id": 2, "name": "Mouse", "price": 25.75, "in_stock": False},
]


@app.route('/login', methods=['POST'])
def login():
    auth = request.json
    username = auth.get("username")
    password = auth.get("password")

    print(username in USERS)
    if username in USERS and USERS[username] == password:
        # Generate a token valid for 1 hour
        token = jwt.encode(
            {"username": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify({"token": token})

    return jsonify({"error": "Invalid credentials"}), 401

def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is missing"}), 401
        
        
        try:
            token = token.split(" ")[1] 
            print(f"Extracted Token: {token}")
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return func(*args, **kwargs)
    return wrapper


@app.route("/products", methods=["GET"])
@token_required
def get_products():
    # print(request.headers)
    in_stock = request.args.get("in_stock")
    if in_stock is not None:
        in_stock = in_stock.lower() == "true"
        filtered_products = [p for p in PRODUCTS if p["in_stock"] == in_stock]
        return jsonify(filtered_products)
    return jsonify(PRODUCTS)


@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    if not data or "name" not in data or "price" not in data or "in_stock" not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_product = {
        "id": len(PRODUCTS) + 1,
        "name": data["name"],
        "price": data["price"],
        "in_stock": data["in_stock"],
    }
    PRODUCTS.append(new_product)
    return jsonify(new_product), 201

if __name__ == "__main__":
    app.run(debug=True)
