from flask import Flask, request, jsonify

from RS import get_predicted_value, get_all_information

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    array = request.json
    predicted_disease = get_predicted_value(array)  # Pass the array to text_extraction
    description, precaution, medication, diet, wrkout = get_all_information(predicted_disease)
    return jsonify([predicted_disease, description, precaution, medication, diet, wrkout])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
