import os
import sys

def parse_exceptions(file_name):
    pass
 
def parse_repo(clone_url):
    dir_name = clone_url.split("/")[-1].split(".")[0]
    print dir_name
    cmd = "rm -rf "+dir_name
    os.system(cmd)
    cmd = "git clone "+clone_url
    os.system(cmd)
    walk_dir = dir_name
    for root, subdirs, files in os.walk(walk_dir):
         for filename in files:
               suffix = ".py"
               if filename.endswith(suffix):
                  file_path = os.path.join(root, filename)
                  print('\t- file %s (full path: %s)' % (filename, file_path))
    cmd = "rm -rf "+dir_name
    os.system(cmd)



cmd = './curl_all.sh'

os.system(cmd)

with open("repos.txt") as f:
    for line in f:
        parse_repo(line) 


