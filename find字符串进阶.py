str1 = 'I think i can do nnnnnnn nn it!'

one = str1.find('!')

print(one)

char_list = list(str1)

for index,value in enumerate(char_list):
    print(index,value)

two = str1.rfind('n')
print(two)



