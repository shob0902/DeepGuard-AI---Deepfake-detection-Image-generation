from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import torch
from torchvision import transforms, models

app = Flask(__name__, template_folder='templates')
CORS(app)

# Load model
model = models.resnet18(pretrained=False)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 2)

checkpoint = torch.load('best_deepfake_resnet18.pth', map_location="cpu")
model.load_state_dict(checkpoint['model_state_dict'])
model.eval()

# Class names
class_names = ['Fake', 'Real']

# Image transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Serve HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Handle prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    image = Image.open(file.stream).convert('RGB')
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)
        # raw scores (logits)
        logits = outputs.squeeze(0).tolist()
        # probabilities
        probs = torch.nn.functional.softmax(outputs, dim=1).squeeze(0).tolist()
        _, preds = torch.max(outputs, 1)
        predicted_index = preds.item()
        predicted_class = class_names[predicted_index]

    # Return prediction along with logits and probabilities for debugging
    return jsonify({
        'prediction': predicted_class,
        'predicted_index': predicted_index,
        'logits': [float(round(x, 6)) for x in logits],
        'probabilities': [float(round(x, 6)) for x in probs]
    })

if __name__ == '__main__':
    app.run(debug=True)
