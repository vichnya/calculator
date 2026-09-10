#запуск: python experiments2.py

from prettytable import PrettyTable


def print_results(*args, action=None, result=None):
  """Красивый вывод через PrettyTable"""
   
  if len(args) == 1:
    
    t_value = [lst, action, result]
    t_description = ['Числа', 'Операция', 'Результат']
    
  else:
    t_value = [lst[0], action, lst[1], result]
    t_description = ['Операнд 1', 'Операция', 'Операнд 2', 'Результат'] 

  columns = len(t_description)

  table = PrettyTable(t_description)
  ds_data = t_value[:]

  while ds_data:
    
    table.add_row(ds_data[:columns])
    ds_data = ds_data[columns:]

  print(table)

lst = [2, 3]
print_results(lst, action="+", result = 5)

print_results(2, 3, action="+", result = 5)