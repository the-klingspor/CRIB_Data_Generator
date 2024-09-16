import os
from PIL import Image
import torch
from torchvision import transforms

# Define the path to your folders
folder_base = "background"
num_folders = 8

# Initialize variables to accumulate the means and stds
mean_sum = torch.zeros(3)
std_sum = torch.zeros(3)
total_images = 0

# Define the transformation to convert PIL image to a tensor
transform = transforms.ToTensor()

for i in range(1, num_folders + 1):
    folder_name = os.path.join("backgrounds", f"{folder_base}{i}")
    for img_name in os.listdir(folder_name):
        img_path = os.path.join(folder_name, img_name)
        with Image.open(img_path) as img:
            img = img.convert("RGB")  # Ensure the image is in RGB format
            img_tensor = transform(img)  # Convert image to tensor
            mean_sum += img_tensor.mean(dim=[1, 2])  # Sum channel-wise means
            std_sum += img_tensor.std(dim=[1, 2])    # Sum channel-wise stds
            total_images += 1

# Compute the average mean and std over all images
mean_avg = mean_sum / total_images
std_avg = std_sum / total_images

print(f"Average channel-wise mean: {mean_avg}")
print(f"Average channel-wise std: {std_avg}")