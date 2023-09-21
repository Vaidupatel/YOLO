from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8n.yaml") # If we want to create the new model from scratch then use this

# load a pretrained model (If we are training our existing model than use this)
model = YOLO(r'C:\Users\HP\PycharmProjects\YOLO\runs\detect\train2\weights\best.pt')
save_dir = r"C:\Users\HP\PycharmProjects\YOLO\runs"
# Use the mode(Give the path of config.yaml file in which we have classified the classes)
model.train(data=r"C:\Users\HP\PycharmProjects\YOLO\config.yaml", epochs=1, project=save_dir)  # train the model
