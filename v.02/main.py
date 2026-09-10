

"""Настройки из текстового файла"""
PARAMS = {
        'precision': None,
        'output_type': None,
        'possible_types': None,
        'dest': None
}

def main():

  load_params()

  print(
"""
Калькулятор с действиями
      
  '+' - Сложение;
  '-' - Вычитание;
  '*' - Умножение;
  '/' - Деление;
  '^' - Возведение в степень;
  '//' - Деление без остатка;
  '%' - Деление по модулю; 

"""
    )
  
  try:
    operand1 = int(input("Оператор 1: "))
    operand2 = int(input("Операнд 2: "))
    sign = input("Оператор: ")   
  except ValueError:
    print('Проверьте вводимые значение на правильность: вводить необходимо числа') 

  

  Calculator(operand1, operand2, sign)
  print()
  
  print("Поиск среднеквадратичного отклонения\n")
  standard_deviation()


def load_params(file="params.ini"):
  """Перенос из текстового файла в словарь"""

  global PARAMS
  f = open(file, mode='r', errors='ignore')
  lines = f.readlines()

  for l in lines:
      param = l.split('=')  
      param[1] = param[1].strip('\n')

      if param[0] != 'dest':
          param[1] = eval(param[1])
                             

      PARAMS[param[0]] = param[1]
      

def convert_precision(precision = None):
  """Счет знаков после запятой"""
  
  global PARAMS
  precision = PARAMS['precision']
  
  def count_func1(search):  
    count = 0
    i = search + 1
    while i < len(string):
      count += 1
      i += 1
    
    return count
  
  def count_func2(search):
    i = search + 1
    gluing = ""
    while i < len(string):
      gluing += string[i]
      i += 1
    gluing = int(gluing)
    return gluing

    
  string = str(precision)
  search1 = string.find(".")
  search2 = string.find("-")
  
  if search1 > 0: 
    return count_func1(search1)
  elif search2 > 0:
    return count_func2(search2)
  else:
    return 0


def standard_deviation(precision = None):
  """Среднеквадратичное отклонение с заданной точностью"""

  global PARAMS
  precision = PARAMS['precision']
  
  import math
  try:
    number_count = int(input("Введите количество числел: "))
    if number_count <= 1 and number_count is int:
      print("Введите количество значений больше одного")
    else:
      args_list = [float(input(f'Введите {i} число: ')) for i in range(1, number_count + 1)]
      print(args_list)
  except ValueError:
      print('Проверьте вводимые значение на правильность: вводить необходимо целые числа') 
    
  sum1 = 0  
  sum1 += sum(x for x in args_list)
  
  x_mean = sum1/len(args_list)

  sum2 = 0
  sum2 += sum((y - x_mean) ** 2 for y in args_list)

  s_d = math.sqrt(sum2/len(args_list))
  result = round(s_d, convert_precision(precision))

  write_log(args_list,
          action='Среднеквадратичное отклонение',
          result=result)
  return print(f'Результат: {result}')


def product(args, precision = None):
  """Приведение к заданной точности"""

  global PARAMS
  precision = PARAMS['precision']

  result = args

  ndigits = convert_precision(precision)
  result = round(result, ndigits)
    
  return result


def Calculator(op1, op2, act):
  """Калькулятор с действиями"""

  if act == "+":
      r = op1 + op2
  
  elif act == "-":
      r = op1 - op2
  
  elif act == "*":
      r = op1 * op2
  
  elif act == "/":
      if op2 != 0:
          r = op1 / op2
      else:
          r = "Деление на ноль не реализуется"
      
  elif act == "^":
    if op1 == 0 and op2 < 0:
      r= "Возведение 0 в отрицательную степень не реализуется"
    else:
      r = op1**op2
  
  elif act == "//":
      r = op1 // op2
  
  elif act == "%":
      r = op1 % op2
  else:
      r = "Операция не распознана"

  write_log(op1, op2, action=act, result=r)
  return print(f'\nРезультат: {r}')

#cделать для всего
def calculate(*args, **kwargs):
  """Сложение чисел с определенной точностью"""

  precision = convert_precision(kwargs['precision'])
  output_type = kwargs['output_type']
  
  i = 0
  result_sum = 0
  while i < len(args):
    result_sum += float(args[i])
    i += 1
  if type(result_sum) is not output_type:
      result_sum = output_type(result_sum)

  return round(result_sum, precision)


def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
  """Запись истории в файл"""
  
  import datetime

  f = open(file, mode='a', errors='ignore')
  date =  datetime.datetime.today()
  args_lst = [x for x in args]
    
# 206-213 упростить(к единообразному виду)
  
  if len(args_lst) == 1:
    f.write(
        f'Дата: {date.strftime("%d/%m/%Y")}    Время:{date.strftime("%H:%M:%S")} \n{action}: {args_lst[0]} = {result} \n\n'
  )
  else:
    f.write(
        f'Дата: {date.strftime("%d/%m/%Y")}    Время: {date.strftime("%H:%M:%S")} \nОперация: {args[0]} {action} {args[1]}  = {result} \n\n'
  )
  f.close()


if __name__ == "__main__":
    from tests import all_tests
    all_tests()

    main()