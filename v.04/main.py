

SETTINGS = {'op1': 1, 'op2': 1, 'op3': 1, 'op4': 1, 'op5': 1}
PARAMS = {'precision': None, 'dest': None}


def load(file="params.ini"):
  """Перенос из текстового файла в словарь"""

  global PARAMS, SETTINGS
  f = open(file, mode='r', errors='ignore')
  lines = f.readlines()

  for l in lines:
      load_value = l.split('=')
      load_value[1] = load_value[1].strip('\n')

      if load_value[0] != 'dest':
          load_value[1] = eval(load_value[1])
      if file == "params.ini":
          PARAMS[load_value[0]] = load_value[1]
      elif file == "settings.ini":
          SETTINGS[load_value[0]] = load_value[1]


def write_log(*args, action = None, result = None, file = 'calc-history.log.txt', full_blok = False):
  """Функция для записи в лог-файла"""
  
  import datetime
  import os
  import stat

  filename = 'newoutput.txt'
  filename2 = 'newoutput.txt.txt'
  new_permissions = stat.S_ENFMT #блок
  os.chmod(filename, new_permissions)
  if full_blok == True:
    os.chmod(filename2, new_permissions)

  date = datetime.datetime.today()
  error = None

  try:

      f = open(file, mode='a', errors='ignore')
      f.write(f'Прогон программы \n')
      f.write(f'Дата {date.strftime("%d/%m/%Y")}\n')
      f.write(f'Время {date.strftime("%H/%M/%S")} \n')
      f.write(f'Операция {action}: {args} = {result} \n')

  except PermissionError:
      print(f'Ошибка записи в файл {file}')
      file_new = file + '.txt'
      print(f'Попытка записать лог в файл с новым именем: {file_new}')
      try:
          with open(file_new, mode='a', errors='ignore') as backup_file:
              backup_file.write(f"{action}: {args} = {result} \n")
      except PermissionError as e:
          error = e
  else:
      f.close()

  if error:
      raise Exception(f'Ошибка записи в файл {file_new}. Записать не удалось.')


def calculate(**kwargs):
  """Функция для вычислений"""

  args = [arg for arg in kwargs.values()]
  res = sum(args)

  write_log(*args, action='sum', result=res)
  print(f'Операция sum: {args} = {res} \nРезультат: {res}')

  return

def main():

  global PARAMS, SETTINGS

  load(file="params.ini")
  load(file="settings.ini")

  calculate(**SETTINGS)

  print("""

Для изменения параметров суммирования измените значения в файле settings.ini

      """)
  
  main()