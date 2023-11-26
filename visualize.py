import open3d
import numpy as np
import torch

def draw_scenes(points, file_name=None, gt_boxes=None, gt_labels=None, ref_boxes=None, ref_labels=None, ref_scores=None,
                point_colors=None,
                draw_origin=True):
    if isinstance(points, torch.Tensor):
        points = points.cpu().numpy()
    if isinstance(gt_boxes, torch.Tensor):
        gt_boxes = gt_boxes.cpu().numpy()
    if isinstance(ref_boxes, torch.Tensor):
        ref_boxes = ref_boxes.cpu().numpy()
    vis=open3d.visualization.Visualizer()
    vis.create_window()
    vis.get_render_option().point_size = 1.0
    vis.get_render_option().background_color = np.zeros(3)
    if draw_origin:
        axis_pcd = open3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])
        vis.add_geometry(axis_pcd)
    pts = open3d.geometry.PointCloud()

    pts.points = open3d.utility.Vector3dVector(points[:, :3])

    vis.add_geometry(pts)
    # view_control = vis.get_view_control()
    # view_control.set_lookat(np.array([0, 0, 0]))
    # view_control.set_up((0, 1, 1))
    # view_control.set_front((0, 0, 0))
    # view_control.rotate(0, 0)
    # view_control.change_field_of_view(step=20)
    if point_colors is None:
        pts.colors = open3d.utility.Vector3dVector(np.ones((points.shape[0], 3)))
    # else:
    #     pts.colors = open3d.utility.Vector3dVector(point_colors)

    vis.run()
    vis.destroy_window()