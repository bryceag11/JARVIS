#https://towardsdatascience.com/guide-to-real-time-visualisation-of-massive-3d-point-clouds-in-python-ea6f00241ee0
import numpy as np
import laspy as lp
import open3d as o3d

dirpath="/home/sakire/Documenti/python3/opengl/lidar/scan/"
dataname="room3d-1.xyz"
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

#Try Open3d ok

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
#pcd.colors = o3d.utility.Vector3dVector(colors/65535)
#pcd.normals = o3d.utility.Vector3dVector(normals)
o3d.visualization.draw_geometries([pcd])
