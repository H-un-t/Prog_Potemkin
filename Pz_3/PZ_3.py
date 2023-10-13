# Вариант 20
i = 0
while i == 0:
 try:
  z = int(input("введите первое число ->"))
  x = int(input("введите второе число ->"))
  c = int(input("введите третье число ->"))
  if z*x < 0 or z*c < 0 or x*c < 0 or x*z < 0 or z*c < 0 or c*x < 0:
    print("<ИСТИНА>")
  else:
    print("<ЛОЖЬ>")
  i = 1
 except ValueError:
    print("Нужно ввести число")