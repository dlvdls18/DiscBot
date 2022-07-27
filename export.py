import os
import base
import lang

print('Preparing source files...')
src_raw = os.listdir('src/')
src = {}
for file in src_raw:
  text = ''
  with open('src/' + file, 'r') as line: text += line.read()
  src[file] = {
    'raw': text,
    'base': {},
    'event': '',
    'lang': {},
    'py': ''
  }

print('Preparing resources...')
res_raw = os.listdir('res/')
res = {}
for file in res_raw:
  text = ''
  with open('res/' + file, 'r') as line: text += line.read()
  res[file] = text
if res['token.txt'] == None:
  print('E: File token.txt does not exist')
  exit(1)

print('Translating...')
for file in src:
  src[file]['base'] = base.BaseLang(src[file]['raw'])[0]
  src[file]['event'] = base.BaseLang(src[file]['raw'])[1]
  fbase = src[file]['base']
  for cmd in fbase: src[file]['lang'][cmd] = lang.Lang('\n'.join(fbase[cmd]))

print('Using template...')
for file in src:
  fbase = src[file]['base']
  text = ''
  for cmd in fbase:
    text += f'if msg.content.split(" ")[0] == "{cmd}": '
    text += '{\n'
    text += src[file]['lang'][cmd]
    text += '}\n'
  clean = []
  lines = text.split('\n')
  li = 0
  for line in lines:
    if li != 0: clean.append('    ' + line)
    else: clean.append(line)
    li += 1
  for line in src[file]['event']: clean.append('   ' + line)
  text = '\n'.join(clean)
  text = lang.itemclean(text)
  ntext = []
  lines = text.split('\n')
  for line in lines:
    if len(line.strip()) != 0: ntext.append(line)
  text = '\n'.join(ntext)
  temp = ''
  with open('temp.py', 'r') as line: temp += line.read()
  temp = temp.replace('$1', text)
  token = ''
  with open('res/token.txt', 'r') as line: token += line.read()
  temp = temp.replace('$2', token)
  src[file]['py'] = temp

print('Exporting source files...')
os.system('rm -r dev')
os.system('mkdir dev')
for file in src:
  filename = file
  if file.endswith('.dbot'): filename = file[0:file.rfind('.')] + '.py'
  f = open('dev/' + filename, 'x')
  f.write(src[file]['py'])
  f.close()

print()
print('Export complete')
print('View the directory dev/')