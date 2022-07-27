import re

def BaseLang(text):
  cmds = {}
  lines = text.split('\n')
  last_cmd = None
  event = []
  for line in lines:
    line = line.strip()
    if len(line) != 0:
      if re.match(r'^(.+)\:$', line):
        name = re.match(r'^(.+)\:$', line).groups()[0]
        last_cmd = name
        cmds[name] = []
      else:
        if last_cmd == None: event.append(line)
        else: cmds[last_cmd].append(line)
  return [cmds, event]