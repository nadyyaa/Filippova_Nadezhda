import csv

with open('songs.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=';')
    answer = list(reader)[1:]
    for streams, artist_name, track_name, date in answer:
        day = int(date[0] + date[1])
        month = int(date[3] + date[4])
        year = int(date[6] + date[7] + date[8] + date[9])
        if streams == 'unknown':
            ln = len(artist_name)
            ls = len(track_name)
            dn = '12.05.23'
            di = date
            rasn = (2023 - year) * 365 + (5 - month) * 30 - (12 - day)
            t = abs(rasn / (ln + ls))
            streams = t
        if year < 2002 or date == '01.01.2002':
            print(f'{track_name} - {artist_name} - {streams}')

with open('songs_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.writer(file)
    w.writerow(['streams', 'artist_name', 'track_name', 'date'])
    w.writerows(answer)