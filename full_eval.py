#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use 
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

import time
import os
from argparse import ArgumentParser

mipnerf360_outdoor_scenes = ["bicycle", "flowers", "garden", "stump", "treehill"]
mipnerf360_indoor_scenes = ["room", "counter", "kitchen", "bonsai"]
tanks_and_temples_scenes = ["truck", "train"]
deep_blending_scenes = ["drjohnson", "playroom"]
nerf_synthetic_scenes = ["chair", "drums", "ficus", "hotdog", "lego", "materials", "mic", "ship"]

parser = ArgumentParser(description="Full evaluation script parameters")
parser.add_argument("--skip_training", action="store_true")
parser.add_argument("--skip_rendering", action="store_true")
parser.add_argument("--skip_metrics", action="store_true")
parser.add_argument("--output_path", default="./eval")
args, _ = parser.parse_known_args()

all_scenes = []
all_scenes.extend(mipnerf360_outdoor_scenes)
all_scenes.extend(mipnerf360_indoor_scenes)
all_scenes.extend(tanks_and_temples_scenes)
all_scenes.extend(deep_blending_scenes)
all_scenes.extend(nerf_synthetic_scenes)

if not args.skip_rendering:
    all_sources = []
    for scene in mipnerf360_outdoor_scenes:
        all_sources.append("/home/bert/datasets/360_v2/" + scene)
    for scene in mipnerf360_indoor_scenes:
        all_sources.append("/home/bert/datasets/360_v2/" + scene)
    for scene in tanks_and_temples_scenes:
        all_sources.append("/home/bert/datasets/tandt/" + scene)
    for scene in deep_blending_scenes:
       all_sources.append("/home/bert/datasets/db/" + scene)
    for scene in nerf_synthetic_scenes:
        all_sources.append("/home/bert/datasets/nerf_synthetic/" + scene)

    common_args = " --quiet --eval --skip_train --sh_degree 2"
    for scene, source in zip(all_scenes, all_sources):
        print(scene, source)
        # os.system("python render.py --iteration 7000 -s " + source + " -m " + args.output_path + "/" + scene + common_args)
        # os.system("python render.py --iteration 30000 -s " + source + " -m " + args.output_path + "/" + scene + common_args)
        
        # os.system("python render.py --iteration 41001 -m /home/bert/datasets/models/" + scene + common_args)
        # os.system("python render.py --iteration 41002 -m /home/bert/datasets/models/" + scene + common_args)
        # os.system("python render.py --iteration 41003 -m /home/bert/datasets/models/" + scene + common_args)
        # scene = "garden"
        # for i in range(25):
        #     os.system("python render.py --iteration " + str(i) + " -m /home/bert/Projects/LightGaussian/output/360_v2/garden_4_" + common_args)
        #    time.sleep(0.5)
        # os.system("python metrics.py -m /home/bert/Projects/LightGaussian/output/360_v2/garden_4_")
        time.sleep(0.5)

if not args.skip_metrics:
    print("EVAL")
    scenes_string = ""
    for scene in all_scenes:
        scenes_string += "\"/home/bert/datasets/models/" + scene + "\" "

    os.system("python metrics.py -m " + scenes_string)