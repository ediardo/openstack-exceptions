import os
import sys
import re
import json
import inspect
from cinder import exception

def get_exception_msg(variable_name):
    global line_buffer
#    variable_name = variable_name +" ="
    #import pdb;pdb.set_trace();
    msg_buffer = []
    for i in reversed(line_buffer):
        if variable_name +" =" in i or variable_name +"=" in i:
#           import pdb; pdb.set_trace();
           line = i
           line = line.strip()
           line = line.replace(variable_name+" = ","")
           line = line.replace(variable_name +"=","")
           line = line.replace("(_(","")
           line = line.replace("_(","")
           line = line.replace(')"',"")
           line = line.replace('"',"")
           line = line.strip()
           #print line
           line_buffer = []
           return line
#           for j in reversed(msg_buffer):
#               print j
        else:
           msg_buffer.append(i)

def parse_exception(line):
    global except_started
    global exc
    global line_buffer
#    line_buffer.append(line)
#    print line
#    import pdb; pdb.set_trace()
    if except_started:
       if "raise exception" in line:
#           print line
#           import pdb;pdb.set_trace();
#           print line
           match = re.search(r"raise exception.(.*)", line)
           if match:
#               import pdb; pdb.set_trace();
               line = match.group(1)
               exception_name = line.split("(")[0]
               use_default = False
               try:
                   variable_name = line.split("=")[1].replace(")","")
   #               import pdb;pdb.set_trace();
                   message = get_exception_msg(variable_name)
               except:
#                   import pdb; pdb.set_trace();
                   use_default = True
               try:
                    if inspect.isclass(getattr(exception, exception_name)):
                        if not exception_name.startswith('_'):
#                          print exception
#                          print exception_name
#                          if "Error" in exception_name:
#                              import pdb;pdb.set_trace();
                             if use_default:
                                 return
                                 message = getattr(exception, exception_name).message
                                 print message
                             try:
                                 exc.append({'name': exception_name,
                                 'code': getattr(exception, exception_name).code,
                                 'msg': message})
                                 #import pdb;pdb.set_trace();
                             except:
                                 return
               except:
                    return
                    #import pdb;pdb.set_trace(); 
           return
    line_buffer.append(line)

def parse_repo(clone_url):
    global except_started
    global exc
    global line_buffer
    dir_name = clone_url.split("/")[-1].split(".")[0]
#    print dir_name
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
                  #print('\t- file %s (full path: %s)' % (filename, file_path))
                  line_buffer = []
                  #import pdb;pdb.set_trace();
                  with open(file_path) as f:
                      for line in f:
                          parse_exception(line)
    cmd = "rm -rf "+dir_name
    os.system(cmd)




clone_url = "https://github.com/openstack/cinder.git"
dir_name = clone_url.split("/")[-1].split(".")[0]
cmd = "rm -rf "+dir_name
#os.system(cmd)
cmd = "git clone "+clone_url
#os.system(cmd)

except_started = True
exc = []
line_buffer = []

parse_repo(clone_url)
#import pdb;pdb.set_trace();

#with open("cinder/cinder/volume/drivers/hitachi/hnas_utils.py") as f:
#    for line in f:
#        parse_exception(line) 
print json.dumps({'cinder': exc})

#print exc
