"""
File Name: opengl_viewer.py

Description: This script reads a .xyz file containing 3D point cloud data and visualizes it in real-time 
             using the Open3D library. It demonstrates how to create a 3D point cloud visualization from 
             the provided point data.
             https://towardsdatascience.com/guide-to-real-time-visualisation-of-massive-3d-point-clouds-in-python-ea6f00241ee0

Usage: Place your .xyz file in the specified directory and adjust the 'dataname' variable to match the file name. 
       Make sure to have the required libraries (numpy, laspy, open3d) installed.

Author: Bryce Grant

Class: EE491 (ECE Capstone II)
"""

import numpy as np
import laspy as lp
import open3d as o3d

# specify data path for .xyz file

dirpath="/home/ROBB/SLAM_Visualization/scan/"
dataname="fpat672.xyz"
path=dirpath+dataname

f = open(path,"r")
lines = f.readlines()
points = []
for l in lines:
    if l[0] != "/":
        x,y,z = l.strip().split()
        points.append( (float(x),float(y),float(z)) )

#factor=10
#decimated_points_random = points[::factor]

# try Open3d


pcd = o3d.geometry.PointCloud() # creating point cloud object
pcd.points = o3d.utility.Vector3dVector(points)
#pcd.colors = o3d.utility.Vector3dVector(colors/65535)
#pcd.normals = o3d.utility.Vector3dVector(normals)


o3d.visualization.draw_geometries([pcd]) # visualize point cloud 
