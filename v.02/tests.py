from main import load_params , calculate, PARAMS


def test_loading_params(test, result):
  """Тест на считывание настроек"""
  load_params()
  assert PARAMS.get(test) == result, "Имя файла для записи истории вызовов функции calculate должно быть output.txt"
  
def test_packed_calc_sum(result, *args, **kwargs):
  """Тест на сложение чисел с определенной точностью"""
  assert calculate(*args, **kwargs) == result, "float round"

def all_tests():
  """Вызов тестов"""
  test_loading_params('dest', 'output.txt')
  test_packed_calc_sum(6.000053, 1.000001, 2.000002, 3.00005, **PARAMS)