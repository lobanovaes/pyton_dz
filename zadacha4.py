# 4-Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
#Пример:
#quarter = 1 => x∈(0, ∞) u y∈(0,∞)

quarter = int(input('введите  номер четверти: '))
if quarter == 1:
    print('quarte = 1 => x>0 , y>0')
elif quarter == 2:
    print('quarte = 2 => x<0 , y>0')
elif quarter == 3:
    print('quarte = 3 => x<0 , y<0')
elif quarter == 4:
    print('quarte = 4 => x>0 , y<0')
else:
    print('введена не правильная четверть')
