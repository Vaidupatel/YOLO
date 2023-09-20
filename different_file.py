import os

# Define the paths to the 'images' and 'labels' folders
images_folder = r'C:\Users\admin\PycharmProjects\YOLO\xtra\Annonate\crab Grass\images'
labels_folder = r'C:\Users\admin\PycharmProjects\YOLO\xtra\Annonate\crab Grass\labels'

# Get the list of image files and label files
image_files = os.listdir(images_folder)
label_files = os.listdir(labels_folder)

# Extract the file names without extensions for comparison
image_file_names = [os.path.splitext(filename)[0] for filename in image_files]
label_file_names = [os.path.splitext(filename)[0] for filename in label_files]

# Find images without corresponding labels
images_without_labels = [image_name for image_name in image_file_names if image_name not in label_file_names]

# Find labels without corresponding images
labels_without_images = [label_name for label_name in label_file_names if label_name not in image_file_names]

# Print the results
print("Images without labels:")
for image_name in images_without_labels:
    print(image_name)

print("\nLabels without images:")
for label_name in labels_without_images:
    print(label_name)
