# libraries used
import laspy as lp
import numpy as np

# create paths and load data
input_path = "/Users/gashongore/Desktop/Point_Cloud/"
output_path = "/Users/gashongore/Desktop/Point_Cloud/"

# Load the file
dataname = "NZ19_Wellington"
point_cloud = lp.file.File(input_path + dataname + ".las", mode="r")

# this can be changed depending on the type of point cloud data we are getting

# store coordinates in "points", and colors in "colors" variable
points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()

# Initialize the number of voxels to create to fill the space including every point
voxel_size = 6  # because it is a cube, the size of the voxel is 6
nb_voxel = np.ceil((np.max(points, axis=0) - np.min(points, axis=0)) / voxel_size)
# the above np.ceil is used for rounding the voxels number to integers

# nb_vox.as type(int) #this gives you the number of voxels per axis
# Compute the non empty voxels and keep a trace of indexes that we can relate to
# points in order to store points later on.
# Also Sum and count the points in each voxel.
non_empty_voxel_keys, inverse, nb_pts_per_voxel = np.unique(
    ((points - np.min(points, axis=0)) // voxel_size).astype(int), axis=0, return_inverse=True, return_counts=True)
idx_pts_vox_sorted = np.argsort(inverse)
# len(non_empty_voxel_keys) # if you need to display how many no-empty voxels you have

# Here, we loop over non_empty_voxel_keys numpy array to
#       > Store voxel indices as keys in a dictionary
#       > Store the related points as the value of each key
#       > Compute each voxel barycenter and add it to a list
#       > Compute each voxel closest point to the barycenter and add it to a list

voxel_grid = {}
grid_barycenter, grid_candidate_center = [], []
last_seen = 0

for idx, vox in enumerate(non_empty_voxel_keys):
    voxel_grid[tuple(vox)] = points[idx_pts_vox_sorted[last_seen:last_seen + nb_pts_per_voxel[idx]]]
    grid_barycenter.append(np.mean(voxel_grid[tuple(vox)], axis=0))
    grid_candidate_center.append(voxel_grid[tuple(vox)][
                                     np.linalg.norm(voxel_grid[tuple(vox)] - np.mean(voxel_grid[tuple(vox)], axis=0),
                                                    axis=1).argmin()])
    last_seen += nb_pts_per_voxel[idx]

    import matplotlib.pyplot as plt

    # from mpl_toolkits import mplot3d

    factor = 10
    decimated_points = points[::factor]
    decimated_colors = colors[::factor]

    ax = plt.axes(projection='3d')
    ax.scatter(decimated_points[:, 0], decimated_points[:, 1], decimated_points[:, 2], c=decimated_colors / 65535,
               s=0.01)
    plt.show()

    # import timeit
    # timeit.timeit (np.savetxt(output_path + dataname + "_voxel-best_point_%s.xyz" % (voxel_size),
    # grid_candidate_center, delimiter=";",fmt="%s"))
