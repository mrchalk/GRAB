import os
import os.path as osp


root_path = os.getcwd()
for subject_index in range(1, 11):
    output_path = osp.join(root_path, "grab_fbx", f"s{subject_index}")
    os.makedirs(output_path, exist_ok = True)
    _ = os.system(f"D:\\program\\blender3.0.1\\blender -b {root_path}\\grab2fbx.blend --python-text Text -- s{subject_index} {output_path}")
