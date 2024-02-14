import csv

with open('songs.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=';')
    answer = list(reader)[1:]
    """Открытие файла, его представление в виде списка"""
    for streams, artist_name, track_name, date in answer:
        day = int(date[0] + date[1])
        month = int(date[3] + date[4])
        year = int(date[6] + date[7] + date[8] + date[9])
        """Преобразование дня, месяца, года в дате в интовый формат"""
        if streams == 'unknown':
            ln = len(artist_name)
            ls = len(track_name)
            dn = '12.05.23'
            di = date
            rasn = (2023 - year) * 365 + (5 - month) * 30 - (12 - day)
            t = abs(rasn / (ln + ls))
            streams = t
            """Описание на языке Python формулы, по которой вычислятся количество прослушиваний
            ln - количество символов в имени артиста
            ls - количество символов в названии песни
            dn - дата указанная в начале задания
            di - дата выхода песни
            rasn - разнцица дат - количество дней
            """
        if year < 2002 or date == '01.01.2002':
            print(f'{track_name} - {artist_name} - {streams}')
            """Первое задание - вывод песен, у которых дата выхода не позже 01.01.2002"""
with open('songs_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.writer(file)
    w.writerow(['streams', 'artist_name', 'track_name', 'date'])
    w.writerows(answer)
    """Добавление данных в файл songs_new.csv"""
