

op1 = float(input("Операнд 1: "))
op2 = float(input("Операнд 2: "))
act = input("Оператор: ") 


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
    r = op1**op2
  
elif act == "//":
    r = op1 // op2
  
elif act == "%":
    r = op1 % op2
  
else:
    r = "Операция не распознана"
  
print("Результат: " + str(r))