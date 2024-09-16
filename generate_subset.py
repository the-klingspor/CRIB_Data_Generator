import os
import numpy as np
import shutil


def create_subset(input_dir, output_dir, subset_size):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Copy over class_idx.json
    src_class_idx = os.path.join(input_dir, 'class_idx.json')
    dst_class_idx = os.path.join(output_dir, 'class_idx.json')
    shutil.copy(src_class_idx, dst_class_idx)

    # Get list of classes (subdirectories in input_dir)
    classes = [d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))]
    indices = None

    # Loop through each class directory
    for class_name in classes:
        class_input_dir = os.path.join(input_dir, class_name)
        class_output_dir = os.path.join(output_dir, class_name)

        # Ensure the class output directory exists
        os.makedirs(class_output_dir, exist_ok=True)

        # Load the fovs.npy file
        fovs_file = os.path.join(class_input_dir, 'fovs.npy')
        fovs = np.load(fovs_file)

        # Select a random subset of indices
        if indices is None:
            indices = np.random.choice(fovs.shape[0], subset_size, replace=False)
            print("Indices chosen!")

        # Copy the selected images
        for idx in indices:
            src_img = os.path.join(class_input_dir, f'{idx:04d}.png')
            dst_img = os.path.join(class_output_dir, f'{idx:04d}.png')
            shutil.copy(src_img, dst_img)

        # Create the subset of fovs.npy
        fovs_subset = fovs[indices]
        subset_fovs_file = os.path.join(class_output_dir, 'fovs.npy')
        np.save(subset_fovs_file, fovs_subset)

        # Load the bboxes.npy file and copy subset
        bbox_file = os.path.join(class_input_dir, 'bboxes.npy')
        bboxes = np.load(bbox_file)
        bbox_subset = bboxes[indices]
        subset_bbox_file = os.path.join(class_output_dir, 'bboxes.npy')
        np.save(subset_bbox_file, bbox_subset)

        print(f"Processed {class_name}: {subset_size} images copied and fovs_subset.npy created.")


# Example usage
input_dir = '/home/akata/jstrueber72/crib/toys200'
output_dir = '/home/akata/jstrueber72/crib/toys200_mrr'
subset_size = 100  # Number of images to select
create_subset(input_dir, output_dir, subset_size)