#запуск: python3 -m unittest -v test_write_log.py
import unittest
from main import load, write_log
from main import PARAMS

load("params.ini")

class TestSomeFunc(unittest.TestCase):
    def test_creating_file_exception(self):
        args = [1, 2, 3, 4, 5]
        log_file = PARAMS['dest']

        self.assertRaises(Exception,
                          write_log,
                          *args,
                          action='sum',
                          file=log_file)

    def test_creating_file_exception_with_descr(self):
        args = [1, 2, 3, 4, 5]
        log_file = PARAMS['dest']
        full_blok = True
        
        
        regex_text = 'Ошибка записи в файл'
        with self.assertRaisesRegex(Exception, regex_text) as cm:
            write_log(*args, action='sum', file=log_file, full_blok = full_blok)
        

