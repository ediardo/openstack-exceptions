import os
import sys
import re
import json
import inspect
from cinder import exception

def count_initial_spaces(line):
    counter = 0
    for i in line:
       if i == ' ':
          counter = counter + 1
       else:
          return counter

def get_exception_msg(variable_name):
    global line_buffer
    msg_buffer = []
    for i in reversed(line_buffer):
        if variable_name +" =" in i or variable_name +"=" in i or variable_name +" ==" in i or variable_name +"==" in i:
           line = i
           line = line.strip()
           line = line.split(variable_name,1)[-1].replace("=","").strip()
           line = line.replace(variable_name+" = ","")
           line = line.replace(variable_name +"=","")
           line = line.replace(variable_name+" == ","")
           line = line.replace(variable_name +"==","")
           line = line.replace("(_(","")
           line = line.replace("_(","")
           line = line.replace(')"',"")
           line = line.replace('"',"")
           line = line.strip()
           line = line.strip('\'')
           line = line.strip(')')
           line = line.strip()
           line_buffer = []
           for j in reversed(msg_buffer):
               if count_initial_spaces(j) > count_initial_spaces(i):
                    j = j.replace(')"',"")
                    j = j.replace('"',"")
                    j = j.strip()
                    j = j.strip('\'')
                    j = j.strip(')')
                    j = j.strip()
                    line = line +" "+j
           return line
        else:
           msg_buffer.append(i)

def parse_exception(line,lnumber,fname):
    global except_started
    global exc
    global line_buffer
    if except_started:
       if "raise exception" in line:
           match = re.search(r"raise exception.(.*)", line)
           if match:
               line = match.group(1)
               exception_name = line.split("(")[0]
               use_default = False
               try:
                   variable_name = line.split("=")[1].replace(")","")
                   message = get_exception_msg(variable_name)
               except:
                   use_default = True
               try:
                    if inspect.isclass(getattr(exception, exception_name)):
                        if not exception_name.startswith('_'):
                             if use_default:
                                 message = getattr(exception, exception_name).message
                             try:
                                 exc.append({'name': exception_name,
                                 'code': getattr(exception, exception_name).code,
                                 'msg': message.strip(),
                                 'line_number':lnumber,
                                 'file_name':fname})
                             except:
                                 return
               except:
                    return
           return
    line_buffer.append(line)

def parse_repo(clone_url):
    global except_started
    global exc
    global line_buffer
    dir_name = clone_url.split("/")[-1].split(".")[0]
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
#                  print('\t- file %s (full path: %s)' % (filename, file_path))
                  line_buffer = []
                  line_number = 1
                  file_name = file_path
                  with open(file_path) as f:
                      for line in f:
                          parse_exception(line,line_number,file_name)
                          line_number = line_number + 1
    cmd = "rm -rf "+dir_name
    os.system(cmd)




clone_url = "https://github.com/openstack/cinder.git"
cmd = "git clone "+clone_url

except_started = True
exc = []
line_buffer = []

parse_repo(clone_url)
items_set = set()
exceptions_set = set()
result = list()

for obj in exc:
    if obj['msg'] is None:
        if obj['name'] not in exceptions_set:
             obj['msg'] = 'null'
        else:
             continue
    exceptions_set.add(obj['name'])
    json_obj = str(obj['code'])+obj['name']+obj['msg']
    if not json_obj in items_set:
        items_set.add(json_obj)
        result.append(obj)


print json.dumps({'cinder': result})

