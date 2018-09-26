from tools.parser import Parse
from tools.tabler import table_create
from tools.tabler import get_finish_number
from tools.saver import save_csv


def iteration(fstart, sfinish):
    with open(fstart, 'r') as f:
        start = int(f.readline().strip())
    finish = get_finish_number(parser_.parse_finish(sfinish))
    return start, finish


def log(ffinish, flog):
    with open(flog, 'a') as f:
        if k:
            print(f'{finish - start} - всего сайтов просмотрено',
                  f'{finish - start - ero1 - ero2 - ero3} - успешно из них записаны',
                  f'{ero1} - недостаточно данных',
                  f'{ero2} - два бота',
                  f'{ero3} - ошибка в записи',
                  sep='\n', end='\n\n', file=f)
            with open(ffinish, 'w') as t:
                t.write(str(finish))
        else:
            print('Authorization fail', end='\n\n', file=f)


if __name__ == '__main__':

    SITE = 'http://s2.11x11.ru/'
    NAME = '****'
    PASSWORD = '******'
    LOG = './logs/log.txt'
    SFINISH = 'http://s2.11x11.ru/xml/games/history.php?act=fullhistory'
    FFINISH = './logs/last_finish.txt'

    k = 0  # счетчик просмотренных сайтов
    ero1 = ero2 = ero3 = 0  # счетчики ошибок

    parser_ = Parse(SITE, NAME, PASSWORD)
    print(get_finish_number(parser_.parse_finish('http://s2.11x11.ru/xml/games/history.php?act=fullhistory')))
    if parser_.authorization:
        start, finish = iteration(FFINISH, SFINISH)
        for id_page in range(start, finish):  # Здесь цикл по id матчей
            base_url = f'http://s2.11x11.ru/reports/{id_page}'
            table_html = parser_.parse_url(base_url)
            k += 1
            if table_html:
                table_human = table_create(table_html)
                if table_human:
                    ero3 += save_csv(table_human)
                else:
                    ero2 += 1
            else:
                ero1 += 1
    log(FFINISH, LOG)
