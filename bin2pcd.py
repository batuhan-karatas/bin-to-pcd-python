import numpy as np
import struct
from open3d import *
import os

def convert_kitti_bin_to_pcd(binFilePath):
    size_float = 4
    list_pcd = []
    with open(binFilePath, "rb") as f:
        byte = f.read(size_float * 4)
        while byte:
            x, y, z, intensity = struct.unpack("ffff", byte)
            list_pcd.append([x, y, z])
            byte = f.read(size_float * 4)
    np_pcd = np.asarray(list_pcd)
    pcd = open3d.geometry.PointCloud()
    pcd.points = open3d.utility.Vector3dVector(np_pcd)
    return pcd

#bin file directory
path_of_the_directory= "binFiles"

for filename in os.listdir(path_of_the_directory):

    bin_file = os.path.join(path_of_the_directory,filename)

    if os.path.isfile(bin_file):
        print(bin_file[-10:-4])
        # convert
        pcd_ = convert_kitti_bin_to_pcd(bin_file)
        # save
        open3d.io.write_point_cloud("pcdFiles\\" + bin_file[-10:-4] + '.pcd', pcd_, write_ascii=False, compressed=False, print_progress=False)