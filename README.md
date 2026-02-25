# AI-x-ray-bone-age-predication

## Model Overview

This model crops hand radiographs to better standardize the image input for bone age models. The model uses a lightweight MobileNetV3 Small 100 backbone and predicts normalized XYWH coordinates.

RUN THE BELOW CMD

/workspaces/AI-x-ray-bone-age-predication/AI-model (main) $ python run_AI_bone_model.py

OUTPUT IS:
Predicted bone age: 145.15 months
Predicted bone age in years: [[12.095517]]


