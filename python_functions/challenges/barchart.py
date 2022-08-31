# Реализуйте функцию, которая выводит на экран столбчатую диаграмму. Функция
# принимает в качестве параметра последовательность чисел, длина которой равна
# количеству столбцов диаграммы. Размер диаграммы по вертикали должен
# определяться входными данными.


def generate_row(num: int, nums: list[int]) -> str:
    max_value, min_value = max(nums), abs(min(nums))
    if abs(num) == num:
        return (' ' * (max_value - num) +
                '*' * num +
                ' ' * min_value)
    else:
        return (' ' * max_value +
                '#' * abs(num) +
                ' ' * (min_value - abs(num)))


def barchart(nums: list) -> str:
    lines = []
    for num in nums:
        row = generate_row(num, nums)
        lines.append(row)
    barchart = '\n'.join(map(''.join, list(zip(*lines))))
    return barchart


print(barchart([5, 10, -5, -3, 7]))
''' *   
    *   
    *   
    *  *
    *  *
   **  *
   **  *
   **  *
   **  *
   **  *
     ## 
     ## 
     ## 
     #  
     #  '''  # noqa

print(barchart([5, -2, 10, 6, 1, 2, 6, 4, 8, 1, -1, 7, 3, -5, 5]))
'''  *            
     *            
     *     *      
     *     *  *   
     **  * *  *   
   * **  * *  *  *
   * **  ***  *  *
   * **  ***  ** *
   * ** ****  ** *
   * ******** ** *
    #        #  # 
    #           # 
                # 
                # 
                # '''  # noqa
