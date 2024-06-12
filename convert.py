import trimesh
import os

def process_mesh(name):
    mesh = trimesh.load_mesh(name)

    mesh.export(name.replace('ply', 'glb'), file_type='glb')
    return mesh

def merge_2_mesh(pth1, pth2):
    mesh1 = process_mesh(pth1)
    mesh2 = process_mesh(pth2)
    merged_mesh = mesh1 + mesh2
    dir_path, filename = os.path.split(pth1)
    merged_mesh.export(os.path.join(dir_path, "merged.glb"), file_type='glb')

def process_floder(pth):
    floders = os.listdir(pth)
    for floder in floders:
        types = os.listdir(os.path.join(pth, floder))
        for typer in types:
            ply_files = os.listdir(os.path.join(pth, floder, typer))
            merge_2_mesh(os.path.join(pth, floder, typer, ply_files[0]), os.path.join(pth, floder, typer, ply_files[1]))

process_floder("/Users/maoyucheng/Desktop/3D_gene/htmls/vis_v2")