def count_words(file):
    filename = file
    with open(filename, encoding='UTF-8') as f_obj:
        contents = f_obj.read()
        words = contents.split()
        num = str(words).lower().count('alice')
        print(num)


file1 = 'alice.txt'
count_words(file1)
