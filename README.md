# AI-x-ray-bone-age-predication

## Model Overview

This model crops hand radiographs to better standardize the image input for bone age models. The model uses a lightweight MobileNetV3 Small 100 backbone and predicts normalized XYWH coordinates.

RUN THE BELOW CMD

/workspaces/AI-x-ray-bone-age-predication/AI-model (main) $ python run_AI_bone_model.py

OUTPUT IS:
Predicted bone age: 145.15 months
Predicted bone age in years: [[12.095517]]



This model crops hand radiographs to better standardize the image input for bone age models. The model uses a lightweight mobilenetv3_small_100 backbone and predicts normalized xywh coordinates.

<img width="1514" height="2044" alt="test_image" src="https://github.com/user-attachments/assets/b8bd05c4-a5ad-48ad-9e98-01f7470d2ffe" />


The model was trained and validated using 12,592 pediatric hand radiographs from the RSNA Pediatric Bone Age Challenge using an 80%/20% split. On single-fold validation, the model achieved mean absolute errors (normalized coordinates) of:


x: 0.0152
y: 0.0121
w: 0.0261
h: 0.0213


🏥 Clinical Impact

Accuracy: MSE ~25 months² (±5 month typical error range)

Speed: Real-time inference (<1 second per image)

Applications: Pediatric growth assessment, endocrine disorder screening

Support: Assists radiologists in bone age evaluation



🧠 Architecture Components

🏗️ Base Model: ResNet152 (80M+ parameters)

🔄 Pre-training: ImageNet initialization

🎯 Task Head: Custom regression layers

👥 Multi-modal: Image + gender fusion

📐 Input Size: 256×256 RGB images


📊 Performance Metrics

Metric	Value	Interpretation

MSE	~25 months²	±5 month typical error

Training Loss	1567.98 → 25.26	98.4% improvement

Convergence	9 epochs	Stable training

Speed	1.69 it/s	Real-time capable


🎯 Intended Use Cases

<img width="378" height="199" alt="image" src="https://github.com/user-attachments/assets/82d0db34-3361-4b5b-a952-230855226ec4" />




📊 Training Performance

📈 Training Progress

<img width="307" height="239" alt="image" src="https://github.com/user-attachments/assets/ab57d5e4-0d44-4669-90c4-5ac94ac80221" />



📋 Training Configuration

  📦 Dataset: RSNA Bone Age (12,500 images)

  ⏱️ Duration: ~1.5 hours (10 epochs)

  🎯 Optimization: SGD/Adam (details in code)

  📊 Batch Size: ~32 (395 batches/epoch)

  🔄 Best Checkpoint: Epoch 9 (MSE: 24.15)



🧠 CNN Architecture Evolution

Traditional CNNs: AlexNet, VGG → Limited medical imaging performance
ResNet Revolution: Skip connections → Better gradient flow, deeper networks
Medical Adaptations: Transfer learning + domain-specific fine-tuning
Multi-modal Integration: Image + metadata fusion for improved accuracy

⚠️ Important Limitations

🎯 Accuracy Interpretation

MSE ≈ 25 months² means typical errors of ±5 months

🏥 Clinical Considerations

  📋 FDA Status: Not FDA approved - research use only
  
  👨‍⚕️ Professional Oversight: Requires medical supervision
  
  🎯 Population: Validated on RSNA dataset demographics
  
  ⚖️ Bias: May vary across different ethnic groups
  
  🔧 Technical Limitations
  
  📸 Image Quality: Requires clear, properly positioned hand X-rays
  
  👶 Age Range: Optimized for pediatric patients (0-18 years)
  
  💾 Memory: ~1GB RAM required for inference
  
  ⚡ Hardware: GPU recommended for real-time performance
  


🚀 Deployment Options

🔧 Quick Deploy
  Deploy to Hugging Face Spaces AWS SageMaker Google Colab

🐳 Docker Deployment

  FROM pytorch/pytorch:latest
  
  COPY requirements.txt .
  
  RUN pip install -r requirements.txt
  
  COPY . /app
  
  WORKDIR /app
  
  EXPOSE 8000
  
  CMD ["python", "app.py"]
  

☁️ Cloud Integration

  Hugging Face Inference API: Serverless deployment
  
  AWS Lambda: Cost-effective inference
  
  Google Cloud Run: Scalable container deployment
  
  Azure Container Instances: Enterprise integration
  
  📊 Model Card Information
  
  
  📈 Performance Summary
  
  🎯 Task: Bone age regression from hand X-rays
  
  📊 Metric: Mean Squared Error (MSE)
  
  🏆 Score: ~25 months² (±5 month error range)
  
  ⚡ Speed: Real-time inference capability
  
  💾 Size: ~320MB (PyTorch), ONNX compatible
  
  🔬 Training Details
  
  📦 Dataset: RSNA Bone Age (12,500 images)
  
  🏗️ Architecture: ResNet152 + custom regression head
  
  ⚙️ Parameters: 80+ million
  
  📊 Epochs: 10 (best at epoch 9)
  
  🔄 Convergence: 98.4% loss reduction
  
