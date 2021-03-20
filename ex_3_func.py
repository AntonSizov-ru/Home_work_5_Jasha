# Задание 3
# 3.2-3.3

import statistics as st

shows = {'Секретные материалы': 'фантастика', 'Ведьмак': 'фэнтази', 'Клан Сопрано': 'криминал', '24': 'драма',
         'Черное зеркало': 'фантастика', 'Во все тяжкие': 'криминал', 'Игра престолов': 'фэнтази',
         'Карточный домик': 'драма', 'Рик и Морти': 'фантастика'}
ratings = {'Секретные материалы': 0.9, 'Ведьмак': 0.95, 'Клан Сопрано': 0.8, '24': 0.75, 'Черное зеркало': 0.98,
           'Во все тяжкие': 0.85, 'Игра престолов': 0.87, 'Карточный домик': 0.82, 'Рик и Морти': 1}


def to_collection():
    """
    Данная функция находит уникальный жанр, после по этому жанру находит все сериалы, подсчитывает их средний рейтинг и
    выводит полученную информацию в срезе по жанру.
    uniques: Список уникальных жанров;
    outputs: Сисок из ключей словаря shows, хранящий в себе названия сериалов по определенному жанру;
    unique: Определённый уникальный жанр полученный из списка uniques;
    show: Ключ словаря shows;
    genre: Значенеи словаря shows;
    result: Ключ словаря shows определённого жанра полученный для поска его рейтинга в словаре ratings
    analyze: Список из значений в словаре ratings по result;
    count: Число сериалов определённого жанра;
    avg: Средний рейтинг сериалов в срезе по определённому жанру.
    """

    # global count, avg # todo 2 если раскоментить то будет другая ошибка.
    print('Данная программа поможет Вам узнать средний рейтинг среди сериалов разного жанра.\n')
    uniques = list(set(shows.values()))
    while len(uniques) > 0:
        outputs = []
        unique = uniques[0]
        uniques.pop(0)
        for show, genre in shows.items():
            if genre in unique:
                outputs.append(show)
                analyze = []
                count = 0
                for result in outputs:
                    if result in ratings.keys():
                        count += 1
                        analyze.append(ratings[result])
                avg = float(st.mean(analyze)) * 10
                avg = format(avg, '.2f')
        print(f'Всего найдено {count} сериала в жанре {unique}, средний рейтинг составляет {avg} / 10.00.')
        # todo 1 не понимаю что не так с переменными, пробовал делать их глобальными он ругается тогда на другое
        # todo при этом код работает как швейцарские часы.


to_collection()
