from transformers import BertTokenizer, BertForSequenceClassification
from flask import Flask, request, jsonify
import torch.nn.functional as F
import torch


app = Flask(__name__)


tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)
model.load_state_dict(torch.load("models/classify_request.pth"))
model.eval()


@app.route('/predict', methods=['POST'])
def predict():
    content = request.json
    text = content['text']

    # Preprocess and tokenize
    input_ids = tokenizer.encode(text, add_special_tokens=True)
    max_len = 64
    input_ids = input_ids + [0] * (max_len - len(input_ids))
    input_ids = torch.tensor([input_ids])  # Add batch dimension

    # Make prediction
    with torch.no_grad():
        output = model(input_ids)[0]
        probabilities = torch.softmax(output, dim=1)
        prediction = torch.argmax(probabilities, dim=1)
        confidence = probabilities[0][prediction].item()

    # Prepare response
    response = {
        'prediction': int(prediction),
        'confidence': float(confidence)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
