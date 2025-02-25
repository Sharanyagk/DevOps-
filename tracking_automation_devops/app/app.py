from flask import Flask, jsonify
import logging
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize tracking variables
app.start_time = time.time()
app.request_count = 0

@app.route("/")
def home():
    app.request_count += 1
    logger.info("Request received at / endpoint")
    return "Hello from Multi-Cloud App! Automation Effectiveness Tracking in Progress."

@app.route("/metrics")
def metrics():
    uptime = time.time() - app.start_time
    logger.info("Metrics endpoint accessed")
    return jsonify({
        "status": "healthy",
        "uptime": uptime,
        "requests_served": app.request_count
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)