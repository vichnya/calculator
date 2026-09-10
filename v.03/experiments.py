#запуск: python experiments.py


def print_results(*args, action = None, result = None):
  """Красивый вывод через написанную функцию"""

  if len(args) == 1:
          
    t_value = [lst, action, result]
    t_description = ['Числа', 'Операция', 'Результат']
    
  else:
    t_value = [lst[0], action, lst[1], result]
    t_description = ['Операнд 1', 'Операция', 'Операнд 2', 'Результат']  

  data = []
  i = 0
  while i < len(t_description):
    data.append([t_description[i], t_value[i]])
    i += 1

  cols = len(data)  
  rows = len(data[0])  


  
  col_width_1 = []
  for col in range(cols):
      columns = [str(data[col][row]) for row in range(rows)]
      col_width_1.append(len(max(columns, key=len)))

  separator = "+-"
  separator += "-+-".join('-' * n   for n in col_width_1)
  separator += "-+"

  
  lines = []

  for i, row in enumerate(range(rows)): 
    
    result = []
    
    for col in range(cols):
      item = str(data[col][row]).center(col_width_1[col])
      if col == 0:
        result.append("| " + item)
      elif col == cols - 1:
        result.append(item + " |")
      else:
        result.append( item )

    if i == 0:
        lines.append(separator)
    
    lines.append(" | ".join(result))
    
    lines.append(separator)

  print('\n'.join(lines))
  

lst = [2, 3]
print_results(lst, action = "+", result = 5)

print_results(2, 3, action = "+", result = 5)