# Personally Identifiable Information (PII) Detection

## Problem Statement

General Data Protection Regulation (GDPR) compliance predominately centers around Personal Data (Article 4, section 1) or Personal Identifiable Information (PII) in the context of an EU establishment. Identification of Personal Data from unstructured data is very critical. PII can reside in images or text. The project uses deep learning object detection model to detect SSN cards residing in images. The model can be easily extended to detect other PII information like credit cards, pan card, aadhar card, etc. by curating or obtaining a suitable dataset.

## Requirements

1. keras > 2.0
2. imgaug
3. plac
4. opencv

Download the weights [full_yolo_backend.h5](https://drive.google.com/open?id=1B7j4-cL9thRseBjHUbIXQwgsM6dtWs4g) and [full_yolo_ssn.h5](https://drive.google.com/open?id=1p4zFhgzglVTap8iDZbI0Tlx3W6BMRAgi), then place it in the `models/` folder.

## Run

You can execute the demo using the following command:

```shell
python demo.py model/full_yolo_ssn.h5 data/sample_images/ssn_1.jpg
```

