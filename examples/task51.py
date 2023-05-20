# '51. Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для разных
# объектов отличается - то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic
# - это функция, которая принимает объект и вычисляет его характеристику.
# В качестве примера характеристики можно взять проверку
# четности из лекции, а можно придумать свою.

list1 = [1,4,8]

def same_by(characteristic, objects):
    new = list(filter(characteristic, objects))
    print(new)

    if new == objects:
        return True
    return False

def characteristic(x):
    return x%2 == 0

print(same_by(characteristic, list1))


