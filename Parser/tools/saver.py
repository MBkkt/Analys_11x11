import csv


def save_csv(tabl):
    """Сохраняем список в csv файл"""
    FNAME = './data/' + ('table_pvp.csv' if tabl[0] else 'table_pve.csv')

    with open(FNAME, 'a', newline='', encoding='utf-8') as csvfile:
        f = csv.writer(csvfile, delimiter=';')
        try:
            f.writerow((tabl[1],
                        tabl[2][0], tabl[2][1],
                        tabl[3][0], tabl[3][1],
                        tabl[4][0], tabl[4][1],
                        tabl[5][0].replace(' ', '_'), tabl[5][1].replace(' ', '_'),
                        tabl[6][0], tabl[6][1]), )
            return 0
        except Exception:
            return 1
