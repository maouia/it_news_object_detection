from ultralytics import YOLO
import os

class Detector :
    def __init__(self):
        model = "models/yolov8m.pt"
        self.model1 = YOLO(model)

    def class_and_confidences(self,res1):
        model1_classes = []
        model1_confidences = []


        for result in res1:
            boxes = result.boxes.cpu().numpy()
            model1_classes = boxes.cls.tolist()
            model1_confidences = boxes.conf.tolist()

        return model1_classes,model1_confidences


    def convert_to_json(self,classes,confidences):
        json_file ={}
        for i,c in enumerate(classes):
            json_file[int(c)]=confidences[i]
        return json_file


    def single_image_prediction(self,image_path):
        res1 = self.model1.predict(conf=0.5, source=image_path)
        classes,confidences = self.class_and_confidences(res1)
        model_results = self.convert_to_json(classes,confidences)

        return model_results









