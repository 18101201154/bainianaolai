import yaml
import os
#读取yaml数据
def read_yaml_data(file_name):
    with open("./data"+os.sep+file_name,"r",encoding='utf-8') as  f:
        return yaml.load(f)


# def read_yaml_data(file_name):
#     with open(os.getcwd()+os.sep+"data"+os.sep+file_name,"r",encoding="utf=8") as f:
#         return yaml.load(f)


