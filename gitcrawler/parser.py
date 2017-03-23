import os
import sys
import re
import json
import inspect
from cinder import exception


def parse_exception(line):
    global except_started
    global exc
    if "except" in line:
       except_started = True
    if except_started:
       if "raise exception." in line:
#           import pdb;pdb.set_trace();
#           print line
           match = re.search(r"raise exception.(.*)", line)
           if match:
#               import pdb; pdb.set_trace();
               line = match.group(1)
               exception_name = line.split("(")[0]
               if inspect.isclass(getattr(exception, exception_name)):
                    if not exception_name.startswith('_'):
                          exc.append({'name': exception_name,
                          'code': getattr(exception, exception_name).code,
                          'msg': getattr(exception, exception_name).message})
               pass
#           match = re.match(r"^.*\"(.*)\".*$",line)
#           print match.group(1)
           line = line.strip()
           line = line.replace("msg = ","")
           line = line.replace("message = ","")
           line = line.replace("(_(","")
           line = line.replace("_(","")
           line = line.replace(')"',"")
           line = line.replace('"',"")
#           line = line.strip()          
#           print line
       if "LOG.err" in line:
#           print line
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



#cmd = './curl_all.sh'

#os.system(cmd)
except_started = False
exc = []

with open("cinder/volume/drivers/hitachi/hnas_utils.py") as f:
    for line in f:
        parse_exception(line) 

print json.dumps({'cinder': exc})
