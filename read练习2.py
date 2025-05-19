
with open('myfile.txt', 'r', encoding='utf-8') as fp:
    print(fp.read(30))

    print(fp.read(30))

    #print(fp.readline())  readline每次读取一行，里面不用写参数

    #print(fp.readlines()) readlines 读取所有行

    
