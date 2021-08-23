
Tasks 

1. files format parsing in Java and make it work with STARE Algorithm ( https://github.com/kaist-dmlab/STARE.git)


parsing common point cloud data files 

las, ply and pcd (commonly used point cloud data format)

.pcd
.las
.ply 
   
parse the files into raw point cloud data in //store coordinates in "points", and colors in "colors" values
   (x,y,z, Red, Blue and Green )variables

 Dimension: 6


Normaly the Algorithm receive

2. NOTES: this task is implemented in python, need to convert it in java for better integration with STARE

[1]

For a given window

 { 

   1. initially compute the bounding box of the point cloud (i.e. the box dimensions that englobe all the points in the window)

         *Assume we know the characteristics of the data source devices (Point cloud registration capability in the Y (vertical )axis )
          --> for experimentation purpose, this can be obtained from max(y) 

         *the horizontal point cloud lenght is going to be an input parameter

   2. Divide the bounding box into small cubic grids and get the total number of voxel
     
     
 Option one: 
       Compute the number, given the size of a single voxel
 
      1. compute the volume of both the bounding box and the desired volex
      2. number_Voxel=BB_Volume/voxel_Volume= number of voxel
 
 Option two: 
       set the number of desired voxels in the three directions of the bounding box

    voxel_Size= 6
    number_Voxel= (max(x,y,z)- min(x,y,z))/voxel_Size  // return number of voxel per axis

  }
   
[2] Identify empty voxel (this is possible ) as we are keeping the window size constant
     
    int  non_empty_Voxels_key[]; // arrays of voxels_IDs with point clouds
     
    int  empty_Voxels_key[];// arrays of voxels_IDs with point clouds






[3]
   1. Ignore all empty voxel (This can increase the performance on top of the STARE idea of keeping the unchanged density)
       using the empty_Voxels_key;

   



   2. Computer the Density of points in each Voxel using STARE Method (avoid repeating unchanged density ??)

  Detect outliers and remove them





