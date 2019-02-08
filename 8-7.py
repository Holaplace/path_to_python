def make_album(singer,album,num = ''):
    file = {'sing':singer,'alb':album}
    if num:
        file['num'] = num
    return file

name_1 = make_album('we','you')
print(name_1)

name_2 = make_album('you','they',num=15)
print(name_2)

name_3 = make_album('he','she')
print(name_3)