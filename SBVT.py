#!/usr/bin/python3

# SBVT (SmartBin Vision Transformer): is a Vision Transformer wrapper around this pretrained ViT model on Hugging Face:
# https://huggingface.co/edwinpalegre/ee8225-group4-vit-trashnet-enhanced
 
# Summary from its Hugging Face page:

# This model is a fine-tuned version of google/vit-base-patch16-224-in21k on the edwinpalegre/trashnet-enhanced dataset
# Params: 85.8M
# Loss: 0.0793
# Accuracy: 0.9817

from transformers import AutoImageProcessor, AutoModelForImageClassification

class SBVT:
    def __init__(self, processor_dir = '.', model_dir = '.'):
        self.processor = AutoImageProcessor.from_pretrained(processor_dir)
        self.model = AutoModelForImageClassification.from_pretrained(model_dir)
    
    def predict_image(self, image):
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        res = self.model.config.id2label[predicted_class_idx]
        return res
