import csv
import sqlite3
from itertools import chain
import sys


def save_sql(tabl):
    """Сохраняем список в sql таблицу"""
    ans = 1
    with sqlite3.connect('./data/mydatabase.db') as conn:
        cursor = conn.cursor()
        try:
            spec = 'pvp' if tabl[0] else 'pve'
            tabl[1] = [tabl[1]]
            tabl = tabl[1:]
            tabl = list(chain.from_iterable(tabl))
            if spec == 'pvp':
                cursor.execute('INSERT INTO pvp VALUES (?,?,?,?,?,?,?,?,?,?,?)', tabl)
            elif spec == 'pve':
                cursor.execute('INSERT INTO pve VALUES (?,?,?,?,?,?,?,?,?,?,?)', tabl)
            conn.commit()
            ans = 0
        except Exception as e:
            print(e, file=sys.stderr)
    return ans


def save_csv(tabl):
    """Сохраняем список в csv файл"""
    FNAME = './data/' + ('table_pvp.csv' if tabl[0] else 'table_pve.csv')
    ans = 1
    with open(FNAME, 'a', newline='', encoding='utf-8') as csvfile:
        f = csv.writer(csvfile, delimiter=';')
        try:
            f.writerow((tabl[1],
                        tabl[2][0], tabl[2][1],
                        tabl[3][0], tabl[3][1],
                        tabl[4][0], tabl[4][1],
                        tabl[5][0], tabl[5][1],
                        tabl[6][0], tabl[6][1],))
            ans = 0
        except Exception as e:
            print(e, file=sys.stderr)
    return ans
