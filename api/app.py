from flask import Flask
from routes.delivery_routes import delivery_bp

app = Flask(__name__)
app.register_blueprint(delivery_bp, url_prefix="/api/delivery")

if __name__ == "__main__":
    app.run(debug=True)
