# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.artist import Artist
from pylab import xticks, yticks

def Create_trajectory_3D(x_traj0, y_traj0,z_traj0, heading0, stride_lengths, step_headings, delta_height):
    """
        Create trajectory.

        Parameters
        ----------
        x_traj0 : float
        y_traj0 : float
        heading0 : radian
        initial values
        stride_lengths : numpy array including time
        step_headings : numpy array including time
        
        Returns
        -------
        x_traj, y_traj : numpy array
            data without the time column
        """
    x_traj = []
    y_traj = []
    z_traj = []
    heading = []
    for i in range(0, stride_lengths.shape[0]):
        x_traj.append(x_traj0 + stride_lengths[i] * np.cos(heading0 + step_headings[i]))
        y_traj.append(y_traj0 + stride_lengths[i] * np.sin(heading0 + step_headings[i]))
        z_traj.append(z_traj0 + sum(delta_height[:i]))
        x_traj0 = x_traj[i]
        y_traj0 = y_traj[i] 
    return x_traj, y_traj, z_traj


ref = np.genfromtxt('ِZero2fourWaypoints.csv', delimiter=' ', skip_header=0)
delta_height = np.genfromtxt('Zero2fourDeltaHeight.csv', delimiter=' ', skip_header=0)
stride_lengths = np.genfromtxt('Zero2fourStepLengths.csv', delimiter=' ', skip_header=0)
step_headings_fromT = np.genfromtxt('Zero2fourStepHeadigs.csv', delimiter=' ', skip_header=0)

x_traj, y_traj, z_traj = Create_trajectory_3D(ref[0,1],ref[0,2],1.3,20*np.pi/180, stride_lengths, step_headings_fromT, delta_height)



fig = plt.figure()
ax = plt.axes(projection='3d')
plt.plot(ref[:,1],ref[:,2],ref[:,3],'o',color = 'r',label = 'Ref. points')
ax.plot3D(x_traj, y_traj, z_traj,'orange', linewidth=2.0, label = '3D PDR')
locs,labels = xticks()     # xticks
xticks(locs, map(lambda x: "%.1f" % x, locs))
locs,labels = yticks()     # ytikcs
yticks(locs, map(lambda x: "%.1f" % x, locs)) #locs[::2]
#plt.axis('equal')
plt.xlabel('X(m)') 
plt.ylabel('Y(m)')
plt.legend()
ax.view_init(30, 30)
#ax.scatter3D(x_traj, y_traj, z_traj)
plt.show()
