str_1 = 'apple'
str_2 = 'APPLE'
print(str_1 == str_2)
print(str_1 == str_2.lower())

str_3 = '12'
str_4 = '15'
print(str_3 == str_4)
print(str_3 != str_4)
print(str_3 > str_4)
print(str_3 < str_4)
print(str_3 >= str_4)
print(str_3 <= str_4)

print((str_3 > str_4) and (str_3 < str_4))
print((str_3 > str_4) or (str_3 < str_4))

if 'b' not in str_1:
    print('b not in str_1')

if 'a' in str_1:
    print('a in str_1')