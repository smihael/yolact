import yaml
from .config import *
import os.path as osp

dataset_path=osp.join(osp.dirname(__file__),'dataset.yaml')
config_path=osp.join(osp.dirname(__file__),'config.yaml')

with open(dataset_path) as f:
    ds = yaml.load(f,Loader=yaml.FullLoader)

with open(config_path) as f:
    cnf = yaml.load(f,Loader=yaml.FullLoader)

dynamic_dataset = dataset_base.copy(ds)
dynamic_config = yolact_resnet50_config.copy(cnf)
