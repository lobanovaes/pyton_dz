# 3- Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:
#x=34; y=-30 -> 4
x = int(input('введите x: '))
y = int(input('введите y: '))
if x > 0 and y > 0:
    print ('1')
elif x < 0 and y > 0:
    print ('2')
elif x < 0 and y < 0:
    print ('3')
elif x > 0 and y < 0:
    print ('4')
elif x == 0:
    print ('введите x>0 или x<0')
elif y == 0:
    print ('введите y>0 или y<0')
