import os
import cv2

# === Paths ===
images_dir = "augmented/images"
labels_dir = "augmented/labels"
output_dir = "augmented/crops"
classes_file = "classes.txt"

# === Create output directory ===
os.makedirs(output_dir, exist_ok=True)

# === Load class names ===
with open(classes_file, "r") as f:
    classes = [c.strip() for c in f.readlines()]
    
cont = 0
# === Loop through all label files ===
for label_file in os.listdir(labels_dir):
    if not label_file.endswith(".txt"):
        continue

    image_name = os.path.splitext(label_file)[0]
    image_path = os.path.join(images_dir, image_name + ".jpg")

    # Skip if image missing
    if not os.path.exists(image_path):
        print(f"⚠️ Image not found for {label_file}, skipping.")
        continue

    # Load image
    img = cv2.imread(image_path)
    h, w, _ = img.shape

    # Read annotations
    with open(os.path.join(labels_dir, label_file), "r") as f:
        lines = f.readlines()

    # For naming crops
    crop_index = 1

    for line in lines:
        parts = line.strip().split()
        if len(parts) != 5:
            continue  # skip bad lines

        cls_id, x_center, y_center, width, height = map(float, parts)
        cls_id = int(cls_id)
        class_name = classes[cls_id]

        # Convert normalized coords to pixel coords
        x_center *= w
        y_center *= h
        width *= w
        height *= h

        # Get corners
        x1 = int(x_center - width / 2)
        y1 = int(y_center - height / 2)
        x2 = int(x_center + width / 2)
        y2 = int(y_center + height / 2)

        # Clip coordinates
        x1, y1 = max(0, x1), max(0, y1)
        x2, y2 = min(w - 1, x2), min(h - 1, y2)

        # Crop
        crop = img[y1:y2, x1:x2]

        # Skip if empty
        if crop.size == 0:
            continue

        # Save crop
        crop_filename = f"{class_name}_{cont}_{crop_index}.jpg"
        cv2.imwrite(os.path.join(output_dir, crop_filename), crop)
        crop_index += 1
        cont += 1
        
print("✅ Cropping complete! Check the 'crops/' folder.")
