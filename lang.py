import re

objects = [
  ['include', 'import $1', 1],
  ['note', '# $1', 1],
  ['source', '$1', 1],
  ['say', 'await sendMsg($1)', 1],
  ['edit', 'await editMsg($1, $2)', 2],
  ['edited', 'await isEdited($1)', 1],
  ['latency', 'bot.latency * 1000', 0],
  ['wait', 'time.sleep($1)', 1],
  ['pass', 'pass', 0],
  ['message', 'msg.content[msg.index(msg.content.split(" ")[0] + 1:]', 0],
  ['mention', 'msg.author.mention', 0],
  ['author', 'msg.author.name', 0],
  ['channel', 'msg.channel', 0],
  ['date', 'datetime.datetime.now().split(" ")[0]', 0],
  ['now', 'now()', 0],
  ['server', 'discord.Guild.name', 0],
  ['set', 'self._$1 = $2', 2],
  ['get', 'self._$1', 1],
  ['equals', '$1 == $2', 2],
  ['greater', '$1 > $2', 2],
  ['lesser', '$1 < $2', 2],
  ['not', 'not ($1)', 1],
  ['contains', '($1 in $2)', 2],
  ['and', '($1) and ($2)', 2],
  ['or', '($1) or ($2)', 2],
  ['random', 'random.randrange($1, $2)', 2],
  ['length', 'len($1)', 1],
  ['type', 'type($1)', 1],
  ['char', 'chr($1)', 1],
  ['concat', 'str($1) + str($2)', 2],
  ['lower', '$1.lower()', 1],
  ['upper', '$1.upper()', 1],
  ['cut', '$1[$2:$3]', 3],
  ['trim', '$1.strip()', 1],
  ['add', 'int($1 + $2)', 2],
  ['sub', 'int($1 - $2)', 2],
  ['multi', 'int($1 * $2)', 2],
  ['div', 'int($1 / $2)', 2],
  ['mod', 'int($1 % $2)', 2],
  ['inc', 'int($1 + 1)', 0],
  ['dec', 'int($1 - 1)', 0],
  ['repeat', 'str($1 * $2)', 2],
  ['call', '_$1()', 1],
  ['print', 'print($1)', 1],
  ['if', 'if($1): {', 1],
  ['elseif', '}\nelif($1): {', 1],
  ['else', '}\nelse: {', 0],
  ['try', 'try: {', 0],
  ['catch', '}\nexcept: {', 0],
  ['define', 'def _$1(): {', 1],
  ['end', '}', 0]
]

def itemtrim(raw):
  text = ''
  last_char = None
  in_str = False
  is_esc = False
  for char in raw:
    if last_char == '\\' or char == '\\': is_esc = True
    if in_str or char != ' ': text += char
    if char == '"' and not is_esc: in_str = not in_str
    last_char = char
    is_esc = False
  return text

def itemtype(raw):
  if raw.startswith('"') and raw.startswith('"') and len(raw) != 1: return 'str'
  elif re.match(r'-?[0-9]+\.[0-9]+', raw): return 'float'
  elif re.match(r'-?[0-9]+', raw): return 'int'
  elif raw in ['true', 'false'] or re.match(r'(not\s+.+|.+\s+(and|or|==|>|<)\s+.+)', raw): return 'bool'
  elif re.match(r'([a-zA-Z]+)\((.*)\)', raw): return 'obj'

def itemsplit(raw):
  text = ''
  type = None
  raw = itemtrim(raw)
  args = []
  last_char = None
  in_str = False
  param_stack = 0
  is_esc = False
  for char in raw:
    if last_char == '\\' or char == '\\': is_esc = True
    if in_str or char != ' ' or param_stack != 0: text += char
    if char == '"' and not is_esc: in_str = not in_str
    if char == '(' and not is_esc: param_stack += 1
    if char == ')' and not is_esc: param_stack -= 1
    if char == ',' and not is_esc and not in_str and param_stack == 0:
      text = text[0:(len(text) - 1)]
      type = itemtype(text)
      args.append(text)
      text = ''
    last_char = char
    from_str = False
    is_esc = False
  if len(text) != 0:
    type = itemtype(text)
    args.append(text)
    text = ''
  return args

def itemobject(raw):
  match = re.match(r'([a-zA-Z]+)\((.*)\)', raw)
  if match == None: return raw
  return list(match.groups())

def itemtranslate(key, args):
  text = ''
  for obj in list(objects):
    if obj[0] == key:
      if len(args) != obj[2]: return ''
      params = []
      for arg in args:
        val = str(arg)
        type = itemtype(arg)
        if type == None: return ''
        if type == 'obj':
          val = itemtranslate(itemobject(arg)[0], itemsplit(itemobject(arg)[1]))
        params.append(val)
      text = str(obj[1])
      for i in range(len(params)):
        text = text.replace(f'${i + 1}', params[i][1:(len(params[i]) - 1)] if key in ['define', 'set', 'get', 'include', 'note', 'source'] and i == 0 else params[i])
  return text

def itemclean(raw):
  text = []
  indent = 0
  lines = raw.split('\n')
  for line in lines:
    session = ''
    last_char = None
    in_str = False
    is_esc = False
    session += '  ' * indent
    for char in line:
      if last_char == '\\' or char == '\\': is_esc = True
      if not (not in_str and char in ['{', '}']): session += char
      if char == '"' and not is_esc: in_str = not in_str
      if char == '{' and not in_str: indent += 1
      if char == '}' and not in_str: indent -= 1
      last_char = char
      is_esc = False
    text.append(session)
  return '\n'.join(text)

def Lang(text):
  codes = []
  lines = text.strip().split('\n')
  for line in lines:
    line = line.strip()
    if len(line) != 0:
      code = itemtranslate(itemobject(line)[0], itemsplit(itemobject(line)[1]))
      if itemtype(line) == 'obj': codes.append(code)
  return itemclean('\n'.join(codes))