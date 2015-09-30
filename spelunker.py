import sublime, sublime_plugin, json, functools, copy

class SpelunkerCommand(sublime_plugin.TextCommand):
  
  def run(self, edit):
    # NOTE: you have to select the value WITHOUT the quotation marks.
    sublime.status_message('Spelunking!')
    selection = self.view.sel() # (10, 20)
    originalText = self.view.substr(selection[0])
    a = selection[0].a
    b = selection[0].b
    inserted = self.view.insert(edit, a, 'hd8374jfisha93840plq')
    if a < b:
      saltySelection = sublime.Region(a, b + inserted) # (10, 40)
    else:
      saltySelection = sublime.Region(a + inserted, b)  

    selectionText = self.view.substr(saltySelection) # 'heeltjeloi'
    allContent = sublime.Region(0, self.view.size())
    allText = self.view.substr(allContent)
    jsonObj = json.loads(allText)
    self.view.replace(edit, saltySelection, originalText)

    firstPath = pathsToValue(selectionText, jsonObj)[0]
    strPath = '.'.join([str(x) for x in firstPath])
    sublime.set_clipboard('__OBJ__.' + strPath)

    # lodashPath = '_.chain(__OBJ__)' + lodashify(paths[0], selectionText) + '.value()'

    # sublime.set_clipboard(lodashPath)

def pathsToValue(target, obj = 'null'):
  if obj == 'null':
      return [];

  keys = range(len(obj)) if isinstance(obj, list) else list(obj)

  unfixed = [getUnfixed(key, target, obj, pathsToValue) for key in keys]

  return list(filter(lambda arr: len(arr) > 0, functools.reduce(lambda sub1, sub2: list(sub1) + list(sub2), unfixed, [])))

def getUnfixed(key, target, obj, pathToValue):
  value = obj[key]

  if target == value:
      return [[key]]

  elif isinstance(value, list) or isinstance(value, dict):
      return map(lambda subPath: [key] + subPath, pathsToValue(target, value))

  else:
      return [[]]

# def lodashify(path, target):
#   lodashified = ''
  
#   for idx in range(len(path)):

#     if isinstance(path[idx], int) and idx == len(path) - 1:
#       lodashified += '.get(\'' + str(path[idx]) + '\')'

#     elif isinstance(path[idx], int):
#       lodashified += '.find(\'' + path[idx + 1] + '\')'

#     else:
#       lodashified += '.get(\'' + path[idx] + '\')'

#   return lodashified
