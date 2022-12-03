#Дан массив размера N. После каждого отрицательного
#  элемента массива вставьте элемент с нулевым значением.

#пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

a_list = [1,2,-1,-2,1,1]
list = a_list
result = []
for element in a_list:
    result.append(element)
    if element < 0:
        result.append(0)
print(result)