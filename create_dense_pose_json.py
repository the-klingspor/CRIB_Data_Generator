import json
import numpy as np

factor_resolution = 3

obj_pose_dict = {}

# Create FoVs for all four factors - exclude the last one for circular factors
azims = np.linspace(-np.pi, np.pi, factor_resolution + 1)[:-1]
elevs = np.linspace(-np.pi, np.pi, factor_resolution + 1)[:-1]
tilts = np.linspace(-np.pi, np.pi, factor_resolution + 1)[:-1]
scales = np.linspace(0.3, 1.1, factor_resolution)

# Combine all FoV combinations into grid list
grid_scale, grid_azim, grid_elev, grid_tilt = np.meshgrid(scales, azims, elevs, tilts)
poses = np.vstack([grid_azim.ravel(), grid_elev.ravel(), grid_tilt.ravel(), grid_scale.ravel()]).T
pose_list = poses.tolist()

print(f"Number of poses generated: {poses.shape[0]}")

# Write FoV poses to json file
obj_pose_dict['pose_list'] = pose_list

out_string = json.dumps(obj_pose_dict, indent=4)

with open('pose_list.json', 'w') as output_file:
    output_file.write(out_string)

