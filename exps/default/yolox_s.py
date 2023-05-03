#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

import os

from yolox.exp import Exp as MyExp


class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
        #self.data_dir = "/content/YOLOX/datasets/COCO/Yolox_dataset"
        #self.train_ann = "train/labels.json"
        #self.val_ann = "validation/labels.json"
        self.max_epoch = 3
        self.num_classes = 4
