#用一行代码展开该列表 [[1,2],[3,4],[5,6]]，得出[1,2,3,4,5,6]

mm = [[1,2], [3,4], [5,6]]

char_list = [ j for a in mm for j in a]

print(char_list)

kk = [[66,7], [98, 9], [87]]

char_list1 = [ h for g in kk for h in g]

print(char_list1)