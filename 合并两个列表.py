def combine_list(arg1, arg2):
    arg1.extend(arg2)
    return arg1
    #return 会终止函数运行，return之后的代码不再执行
    


list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(combine_list(list1, list2))