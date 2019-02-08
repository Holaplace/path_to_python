def make_album(singer,album,num = ''):
    file = {'sing':singer,'alb':album}
    if num:
        file['num'] = num
    return file

while True:
    singer = input('Singer_name: ')
    if singer == 'q':
        break

    album = input('Album_name: ')
    if album == 'q':
        break

    name_file = make_album(singer,album)
    print(name_file)