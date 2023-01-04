Sergey, Kate = input(), input()
if Sergey == Kate:
    print('ничья')
elif Sergey == 'ножницы' and Kate == 'бумага' or Sergey == 'бумага' and Kate == 'камень' or Sergey == 'камень' and Kate == 'ножницы':
    print('Sergey')
else:
    print('Kate')
