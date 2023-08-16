# Utility-files
These are the utility files that can be used for machine learning models.

## 1. Convert_model.ipynb
This file generates CSV file from ML training output (epochs, loss, acc, val_loss, val_acc).

## 2. yolo_to_csv.ipynb
Generates csv from yolo.log.
* log file contains training log.

## 3. yolo_to_tensorflow.ipynb
Converts yolo.weights to .pb and tflite.

## 4. check_number_of_labels_per_class.ipynb
Using this script we can check number of labels per class by traversing all yolo txt(labels) files.

## 5. copy_files_of_same_class.ipynb
This script checks all label files of yolo and copy only those files having (the specified) class. It copies both image and label.

## 6. moving_and_renaming_files.ipynb
This script movies files from one folder to another folder and also renames the file.
For my work i have to move both image and txt file to another folder. 
Where both files have same name.
##### This script works when images and txt files are in different directories.

## 7. moving_txt_files.ipynb
This script movies files from one folder to another folder according to the images that are present in another location.
It just moves text files in trian test and val folders, text files with same name as image files in train test and val folders.
##### This script works when images and txt files are in different directories.

## 8. remove_class.ipynb
To remove a certain class from yolo labeled data.

## 9. removeclass.py
To remove a certain class from yolo labeled data.

## 10. train_test_spit.ipynb
To split dataset into train test by modulus of total number of files in folder.

## 11. yolo_to_xml.py
Converts yolo labels to xml files

## 12. onnx_to_tflite.ipynb
To convert the onnx file to tflite and tensorflow saved_model (.pb) format.
- pip install onnx_tf
- pip install tensorflow
- pip install opencv-python (optional)

## 13. Tflite model inference
Adjust the inputs and outputs accordingly.
[tflite_testing.ipynb](tflite_testing.ipynb)
