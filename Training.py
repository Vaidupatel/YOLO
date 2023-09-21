from ultralytics import YOLO

# Load a model
model = YOLO(r"C:\Users\Admin\PycharmProjects\YOLO\train\weights\best.pt") # If we want to create the new model from scratch then use this

# load a pretrained model (If we are training our existing model than use this)
# model = YOLO(r'yolov8n.pt')

save_dir = r"C:\Users\Admin\PycharmProjects\YOLO"
# Use the mode(Give the path of config.yaml file in which we have classified the classes)
model.train(data=r"C:\Users\admin\PycharmProjects\YOLO\config.yaml", epochs=10, project=save_dir)  # train the model
