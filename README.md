# DeepFake Detection Project

A deep learning-based web application for detecting deepfake images using transfer learning with ResNet18. The application provides both a machine learning training pipeline and an interactive web interface for real-time predictions.

## 🎯 Project Overview

This project implements a binary classification system to detect whether an image is a **real face** or a **deepfake**. It leverages a pre-trained ResNet18 model fine-tuned on a custom dataset of real and fake facial images.

### Key Features
- **Transfer Learning**: Uses pre-trained ResNet18 from ImageNet for feature extraction
- **Web Interface**: Interactive Flask-based web application for image uploads and predictions
- **Real-time Predictions**: Instant classification results with confidence scores
- **Visualization**: Grad-CAM heatmaps to interpret model decisions
- **Video Support**: Notebook utilities to extract frames from videos for batch analysis

---

## 📋 Project Structure

```
DeepFake/
├── app.py                          # Flask backend application
├── test_pred.py                    # Command-line testing script
├── best_deepfake_resnet18.pth      # Pre-trained model weights
├── requirements.txt                # Python dependencies
├── one.ipynb                       # Model training & evaluation notebook
├── videotophoto.ipynb              # Video frame extraction notebook
├── Dataset/
│   ├── Train/                      # Training data
│   │   ├── Fake/
│   │   └── Real/
│   ├── Validation/                 # Validation data
│   │   ├── Fake/
│   │   └── Real/
│   └── Test/                       # Test data
│       ├── Fake/
│       └── Real/
├── templates/
│   └── index.html                  # Web UI (Frontend)
├── static/                         # Static assets (CSS, JS, images)
└── .github/                        # GitHub configurations
```

---

## 🛠️ Technologies & Tools Used

### Deep Learning & ML
- **PyTorch** - Deep learning framework
  - `torch` - Core tensor library
  - `torchvision` - Computer vision utilities and pre-trained models
  - `torchaudio` - Audio processing
- **ResNet18** - Pre-trained convolutional neural network architecture
- **TorchCAM** - Grad-CAM visualization for model interpretability

### Backend
- **Flask** - Lightweight web framework for Python
- **Flask-CORS** - Cross-Origin Resource Sharing support

### Data Processing & Analysis
- **PIL/Pillow** - Image processing and manipulation
- **NumPy** - Numerical computing
- **OpenCV (cv2)** - Computer vision and video processing
- **scikit-learn** - Machine learning metrics and evaluation
  - `accuracy_score`
  - `confusion_matrix`
  - `classification_report`

### Visualization
- **Matplotlib** - Data visualization and plotting

### Frontend
- **HTML5** - Web interface markup
- **TailwindCSS** - Utility-first CSS framework
- **JavaScript** - Client-side interactivity

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```
torch
torchvision
torchaudio
flask
Flask-Cors
requests
pillow
numpy
opencv-python
scikit-learn
matplotlib
torchcam
```

### Installation

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Running the Web Application

Start the Flask server:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`

**Features:**
- Upload an image via the web interface
- Get instant real-time predictions
- View confidence scores for both "Fake" and "Real" classifications
- Interactive UI with image preview

### 2. Command-Line Testing

Test the API using the provided test script:

```bash
python test_pred.py <path_to_image>
```

Example:
```bash
python test_pred.py Dataset/Test/Real/real_63.jpg
```

**Response:**
```json
{
  "prediction": "Real",
  "predicted_index": 1,
  "logits": [0.123456, 0.876543],
  "probabilities": [0.20, 0.80]
}
```

### 3. Training & Evaluation

Open and run the training notebook:

```bash
jupyter notebook one.ipynb
```

**Notebook Workflow:**
- Data loading and preprocessing
- Model architecture setup with transfer learning
- Training loop with validation
- Test set evaluation
- Performance metrics (accuracy, confusion matrix, classification report)
- Prediction visualization
- Grad-CAM heatmap generation

### 4. Video Frame Extraction

Use the video processing notebook to extract frames:

```bash
jupyter notebook videotophoto.ipynb
```

This utility extracts frames from videos at a specified FPS rate for batch analysis.

---

## 🧠 Model Architecture

### ResNet18 with Transfer Learning

- **Base Model**: ResNet18 pre-trained on ImageNet (1.2M weights)
- **Fine-tuning Strategy**:
  - Freeze all convolutional layers
  - Replace the final fully connected layer
  - Train only the new classification head (Fake vs. Real)
- **Classification Head**: Linear layer mapping 512 features to 2 classes
- **Loss Function**: CrossEntropyLoss
- **Optimizer**: Adam (learning rate: 1e-4)
- **Scheduler**: ReduceLROnPlateau (reduces learning rate when validation accuracy plateaus)

### Input/Output
- **Input**: RGB images resized to 224×224 pixels
- **Normalization**: ImageNet normalization (mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
- **Output**: Binary classification (Fake=0, Real=1) with probability scores

---

## 📊 Dataset

The project uses a structured dataset with three splits:

### Dataset Statistics
- **Training Set**: Images for model training with augmentation
- **Validation Set**: Images for hyperparameter tuning and early stopping
- **Test Set**: Held-out images for final evaluation

### Data Augmentation (Training Only)
- Random horizontal flips (50% probability)
- Random rotations (±10 degrees)
- Image resizing to 224×224
- Tensor conversion and normalization

---

## 📈 Training Configuration

| Parameter | Value |
|-----------|-------|
| Batch Size | 32 |
| Image Size | 224×224 |
| Learning Rate | 1e-4 |
| Number of Epochs | 10 |
| Number of Workers | 4 |
| Loss Function | CrossEntropyLoss |
| Optimizer | Adam |
| Learning Rate Schedule | ReduceLROnPlateau |

---

## 🎨 Web Interface

The frontend (`templates/index.html`) features:

- **Modern Dark Theme**: Built with TailwindCSS gradient background
- **Image Upload**: Drag-and-drop or click to upload images
- **Live Preview**: Image preview before sending to the server
- **Real-time Predictions**: Instant classification results
- **Confidence Scores**: Probability breakdown for both classes
- **Responsive Design**: Mobile-friendly interface

### API Endpoint

**POST** `/predict`
- **Input**: Multipart form data with image file
- **Output**: JSON with prediction, probabilities, and logits

---

## 🔍 Model Interpretability

### Grad-CAM Visualization

The project includes Grad-CAM (Gradient-weighted Class Activation Mapping) for visualizing which regions of the image the model focuses on when making predictions.

Features:
- Heatmap overlay on original images
- Identifies discriminative features for deepfake detection
- Helps understand model decision-making

---

## 📋 File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Flask backend API for serving predictions |
| `one.ipynb` | Complete training and evaluation pipeline |
| `videotophoto.ipynb` | Video frame extraction utility |
| `test_pred.py` | CLI tool for testing predictions |
| `best_deepfake_resnet18.pth` | Pre-trained model checkpoint |
| `templates/index.html` | Web UI frontend |
| `requirements.txt` | Python package dependencies |

---

## 🔧 Configuration

### Hyperparameters (in `one.ipynb`)

Modify these values to adjust training behavior:

```python
BATCH_SIZE = 32
NUM_WORKERS = 4 
IMAGE_SIZE = 224 
LEARNING_RATE = 1e-4
NUM_EPOCHS = 10
```

### Data Path

Update the dataset path in the notebook:

```python
DATA_ROOT = Path(r"C:\Users\YourUsername\Path\To\DeepFake\Dataset")
```

---

## 📊 Performance Metrics

The trained model is evaluated using:

- **Accuracy**: Overall classification accuracy
- **Precision & Recall**: Per-class performance metrics
- **Confusion Matrix**: True positives, false positives, etc.
- **Classification Report**: Detailed breakdown by class
- **Loss Curves**: Training and validation loss tracking

---

## 🚀 Future Improvements

- [ ] Multi-face detection in images
- [ ] Real-time video stream analysis
- [ ] Model ensemble for better accuracy
- [ ] ONNX model export for inference optimization
- [ ] Mobile app version
- [ ] Advanced deepfake detection techniques (face morphing, audio sync, etc.)

---

## ⚠️ Limitations

- Optimized for frontal facial images
- Performance depends on dataset quality and diversity
- May have reduced accuracy on highly realistic deepfakes
- Requires GPU for optimal inference speed

---

## 📝 License

This project is provided as-is for educational and research purposes.

---

## 📧 Contact & Support

For issues, questions, or contributions, please refer to the project documentation or contact the development team.

---

## 🙏 Acknowledgments

- **PyTorch Team** - Deep learning framework
- **TorchVision** - Pre-trained models
- **Flask Community** - Web framework
- **ResNet Authors** - Deep residual learning architecture

---

**Last Updated**: January 2026  
**Project Status**: Active
