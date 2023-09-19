from ultralytics import YOLO


# Load a model
model = YOLO("yolov8n.yaml") # If we want to create the new model from scratch then use this

save_dir = r"C:\Users\admin\PycharmProjects\YOLO"

# load a pretrained model (If we are training our existing model than use this)
# model = YOLO(r'C:\Users\admin\PycharmProjects\YOLO\runs\detect\train\weights\best.pt')

# Use the mode(Give the path of config.yaml file in which we have classified the classes)
model.train(data=r"C:\Users\admin\PycharmProjects\YOLO\config.yaml", project=save_dir, epochs=1)  # train the model
