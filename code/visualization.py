import numpy as np
import matplotlib.pyplot as plt
from transforms3d.euler import mat2euler

def visualize_trajectory_2d(pose, save_path, path_name="Unknown", show_ori=False, show_plot=False):
    fig,ax = plt.subplots(figsize=(5,5))
    n_pose = pose.shape[2]

    ax.plot(pose[0,3,:], pose[1,3,:], 'r-', label=path_name)
    ax.scatter(pose[0,3,0], pose[1,3,0], marker='s', label="start")
    ax.scatter(pose[0,3,-1],pose[1,3,-1], marker='o', label="end")
  
    if show_ori:
        select_ori_index = list(range(0, n_pose,max(int(n_pose / 50), 1)))
        yaw_list = []
        
        for i in select_ori_index:
            _, _, yaw = mat2euler(pose[:3,:3,i])
            yaw_list.append(yaw)
    
        dx = np.cos(yaw_list)
        dy = np.sin(yaw_list)
        dx,dy = [dx,dy]/np.sqrt(dx**2+dy**2)
        ax.quiver(pose[0,3,select_ori_index],pose[1,3,select_ori_index],dx,dy,\
            color="b",units="xy",width=1)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axis('equal')
    ax.grid(False)
    ax.legend()
    # plt.savefig(save_path, dpi=150)

    if show_plot:
        plt.show(block=True)
    # plt.close()

    return fig, ax

def visualize(pose, landmarks, save_path, path_name="slam",show_ori=True, show_plot=False):
    fig,ax = plt.subplots(figsize=(5,5))
    n_pose = pose.shape[2]

    ax.plot(pose[0,3,:], pose[1,3,:], 'r-', label=path_name)
    ax.scatter(pose[0,3,0], pose[1,3,0], marker='s', label="start")
    ax.scatter(pose[0,3,-1], pose[1,3,-1], marker='o', label="end")
    ax.scatter(landmarks[:,0], landmarks[:,1], s=2, marker='o', label="landmarks")

    if show_ori:
        select_ori_index = list(range(0, n_pose, int(n_pose / 50)))
        yaw_list = []
        for i in select_ori_index:
            _,_,yaw = mat2euler(pose[:3,:3,i])
            yaw_list.append(yaw)
        dx = np.cos(yaw_list)
        dy = np.sin(yaw_list)
        dx,dy = [dx,dy] / np.sqrt(dx ** 2 + dy ** 2)
        ax.quiver(pose[0, 3, select_ori_index],pose[1, 3, select_ori_index], dx, dy,\
            color="b", units="xy", width=1)
        
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axis('equal')
    ax.grid(False)
    ax.legend()

    ax.set_aspect('auto')
    ax.set_xlim([-1200, 500])
    ax.set_ylim([-1000, 600])
    # ax.set_xlim([-1000, 300])
    # ax.set_ylim([-500, 700])

    plt.savefig(save_path, dpi=150)
    if show_plot:
        plt.show(block=True)
    # plt.close()
    return fig, ax

def combine_visualize(pose,slam_pose, landmarks, slam_landmarks, save_path, path_name="Unknown", show_ori=False, show_plot=False):
    fig,ax = plt.subplots(figsize=(5,5))
    n_pose = pose.shape[2]

    ax.plot(pose[0,3,:], pose[1,3,:], 'b-', label='orig')
    ax.plot(slam_pose[0,3,:], slam_pose[1,3,:],'r-',label='slam')
    ax.scatter(pose[0,3,0], pose[1,3,0], marker='s', label="start")
    ax.scatter(pose[0,3,-1], pose[1,3,-1], marker='o', label="end")
    ax.scatter(landmarks[:,0], landmarks[:,1], s=2, marker='o', label="landmarks")
    ax.scatter(slam_landmarks[:,0], slam_landmarks[:,1], s=2, marker='o', label="slam_landmarks")
    
    if show_ori:
        select_ori_index = list(range(0,n_pose,int(n_pose/50)))
        yaw_list = []
        for i in select_ori_index:
            _,_,yaw = mat2euler(pose[:3,:3,i])
            yaw_list.append(yaw)
        dx = np.cos(yaw_list)
        dy = np.sin(yaw_list)
        dx,dy = [dx,dy ] /np.sqrt(dx ** 2 + dy ** 2)
        ax.quiver(pose[0, 3, select_ori_index], pose[1, 3, select_ori_index], dx, dy,\
            color="b", units="xy", width=1)
        
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axis('equal')
    ax.grid(False)
    ax.legend()

    ax.set_aspect('auto')
    ax.set_xlim([-1200, 500])
    ax.set_ylim([-1000, 600])
    # ax.set_xlim([-1000, 300])
    # ax.set_ylim([-500, 700])

    plt.savefig(save_path, dpi=150)

    if show_plot:
        plt.show(block=True)
    # plt.close()
    return fig, ax