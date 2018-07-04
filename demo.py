import os
import cv2
import numpy as np
import plac
import json
from yolo2.frontend import YOLO

#Set environment variables to run it on cpu
os.environ['CUDA_DEVICE_ORDER']="PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"]="0"

@plac.annotations(
    weights_path = plac.Annotation("Model path", type=str),
    image_path = plac.Annotation("Image path", type=str)
)
def main(weights_path, image_path):
    if not os.path.exists(weights_path):
        raise Exception("The model file doesn't exist in this path "+str(weights_path))
    
    if not os.path.exists(image_path):
        raise Exception("The image file doesn't exist in this path "+str(image_path))
    
    with open('config.json') as config_buffer:    
        config = json.load(config_buffer)
    
    yolo = YOLO(backend             = config['model']['backend'],
            input_size          = config['model']['input_size'], 
            labels              = config['model']['labels'], 
            max_box_per_image   = config['model']['max_box_per_image'],
            anchors             = config['model']['anchors'])

    yolo.load_weights(weights_path)

    image = cv2.imread(image_path)
    predictions = yolo.predict(image)

    if len(predictions)>0:
        print("SSN card is detected")
    else:
        print("No SSN card detected")
    
if __name__ == '__main__':
    plac.call(main)