from flask import Blueprint, jsonify, request
from utils.helpers import calculate_eta

delivery_bp = Blueprint("delivery", __name__)

@delivery_bp.route("/status", methods=["GET"])
def get_status():
    return jsonify({"status": "Delivery API is running"}), 200

@delivery_bp.route("/eta", methods=["POST"])
def estimate_eta():
    data = request.get_json()
    origin = data.get("origin")
    destination = data.get("destination")
    
    if not origin or not destination:
        return jsonify({"error": "Missing coordinates"}), 400

    eta = calculate_eta(origin, destination)
    return jsonify({"eta_minutes": eta}), 200
