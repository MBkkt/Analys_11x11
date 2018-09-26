import re


def table_create(arr):
    """Разбираем HTML таблицу"""

    ans = []

    a = re.findall(r'Спарринг-Бот', str(arr[1]))
    b = re.findall(r'Спарринг-Бот', str(arr[2]))
    if a and b:
        return ans  # бот-бот
    elif a or b:
        ans.append(0)  # пве
    else:
        ans.append(1)  # пвп

    a, b = map(int, re.findall(r'\d+[:]\d+', str(arr[0]))[0].split(":"))  # счет
    if a > b:  # победа левого
        ans.append(1)
    elif a < b:  # победа правого
        ans.append(0)
    else:  # ничья
        ans.append(0)

    ans.append(re.findall(r'\b\d+[.]?\d+\b', str(arr[5])))  # средняя сила игроков на поле
    ans.append(re.findall(r'\d+', str(arr[7])))  # тактика
    ans.append(re.findall(r'\d+[-]\d+[-]\d+', str(arr[6])))  # схема
    ans.append(re.findall(r'нормальная|дальние удары|техничная игра|игра в пас', str(arr[9])))  # стратегия
    ans.append(re.findall(r'смешанные|дальние|короткие', str(arr[10])))  # передачи
    # ans.append(re.findall(r'да|нет', str(arr[8])))
    # прессинг, отсутвует у большинства матчей, по информации разработчиков ни на что не влияет, также проверил это сам

    return ans


def get_finish_number(html):
    """Получаем номер последнего матча"""
    return int(re.findall(r'\d+', str(html))[0])
