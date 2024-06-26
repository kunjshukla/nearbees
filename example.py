from flask import Flask, request, jsonify
import nearbees # Replace with your flower recognition module

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Flower Recognition System"

@app.route("/upload", methods=["POST"])
def upload():
    # Access uploaded image
    image_file = request.files["image"]
    if image_file:
        # Process image using your flower recognition code
        flower_name = your_flower_recognition_code.recognize_flower(image_file.read())
        return jsonify({"flower_name": flower_name})
    else:
        return jsonify({"error": "No file uploaded"}), 400

if __name__ == "__main__":
    app.run(debug=True)
