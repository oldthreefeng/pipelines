# coding:utf-8
import subprocess, os
def get_filename():
    with open("images.txt", "r") as f:
        lines = f.read().split('\n')
        # print(lines)
        return lines
 
 
def sync_image():
    name_list= get_filename()
    for name in name_list:
        if 'sha256' in name:
            print(name)
            sha256_name = name.split("@")
            new_name = sha256_name[0].split("/")[-1]
            tag = sha256_name[-1].split(":")[-1][0:6]
            image = "registry.cn-hangzhou.aliyuncs.com/mlops-pipeline/" + new_name + ":"+ tag
            cmd = "docker tag {0}   {1}".format(name, image)
            subprocess.call("docker pull {}".format(name), shell=True)
            subprocess.call(["docker", "tag", name, image])
            subprocess.call("docker push {}".format(image), shell=True)
        else:
            new_name = "registry.cn-hangzhou.aliyuncs.com/mlops-pipeline/" + name.split("/")[-1]
            cmd = "docker tag {0}   {1}".format(name, new_name)
            subprocess.call("docker pull {}".format(name), shell=True)
            subprocess.call(["docker", "tag", name, new_name])
            subprocess.call("docker push {}".format(new_name), shell=True)
         
if __name__ == "__main__":
    sync_image()
