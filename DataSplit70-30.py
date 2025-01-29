import os
import shutil
import random

def split_images_and_labels(data_folder, dataset_folder='dataset', split_ratio=0.7):
    
    if not os.path.exists(data_folder):
        print(f"Error: The data folder '{data_folder}' does not exist.")
        return

    
    if not os.path.exists(dataset_folder):
        os.makedirs(dataset_folder)
        print(f"Created dataset folder at '{dataset_folder}'.")

    
    images_folder = os.path.join(dataset_folder, 'images')
    labels_folder = os.path.join(dataset_folder, 'labels')
    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(labels_folder, exist_ok=True)

    
    if not os.path.exists(os.path.join(data_folder, 'images')) or not os.path.exists(os.path.join(data_folder, 'labels')):
        print(f"Error: The data folder must contain both 'images' and 'labels' subfolders.")
        return

    
    image_files = [f for f in os.listdir(os.path.join(data_folder, 'images')) if os.path.isfile(os.path.join(data_folder, 'images', f)) and f.lower().endswith(('.bmp', '.jpeg', '.jpg', '.png'))]
    
    
    random.shuffle(image_files)

    
    split_index = int(len(image_files) * split_ratio)

    
    train_images = image_files[:split_index]
    val_images = image_files[split_index:]

    
    train_images_folder = os.path.join(images_folder, 'train')
    val_images_folder = os.path.join(images_folder, 'val')
    train_labels_folder = os.path.join(labels_folder, 'train')
    val_labels_folder = os.path.join(labels_folder, 'val')

    
    os.makedirs(train_images_folder, exist_ok=True)
    os.makedirs(val_images_folder, exist_ok=True)
    os.makedirs(train_labels_folder, exist_ok=True)
    os.makedirs(val_labels_folder, exist_ok=True)

    
    for image in train_images:
        
        shutil.move(os.path.join(data_folder, 'images', image), os.path.join(train_images_folder, image))
        
        label = os.path.splitext(image)[0] + '.txt'  
        if os.path.exists(os.path.join(data_folder, 'labels', label)):
            shutil.move(os.path.join(data_folder, 'labels', label), os.path.join(train_labels_folder, label))

    for image in val_images:
        
        shutil.move(os.path.join(data_folder, 'images', image), os.path.join(val_images_folder, image))
        
        label = os.path.splitext(image)[0] + '.txt'  
        if os.path.exists(os.path.join(data_folder, 'labels', label)):
            shutil.move(os.path.join(data_folder, 'labels', label), os.path.join(val_labels_folder, label))

    print(f"Moved {len(train_images)} images and labels to train folder.")
    print(f"Moved {len(val_images)} images and labels to val folder.")


data_folder = 'data'  
split_images_and_labels(data_folder)
