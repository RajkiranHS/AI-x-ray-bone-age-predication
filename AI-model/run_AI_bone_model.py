import numpy as np
import cv2 
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('bone_age_model.h5')
img = cv2.imread('test_image.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (224, 224))
img = img / 255.0  # Normalize
img = np.reshape(img, (1, 224, 224, 1))

predicted_age = model.predict(img)
print(f"Predicted bone age: {predicted_age[0][0]:.2f} months")
print("Predicted bone age in years:", predicted_age/12)
