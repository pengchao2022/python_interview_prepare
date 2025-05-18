info = {
    "name":"jeep",
    "age":37,
    "height":181,
    "is_married":"false",
    "girls":[
        #字典是列表里面的元素
        {"name":"liuyifei",
         "age":28,
         "city":"beijing",
         "height":181
         },
         {"name":"boduoye",
         "age":30,
         "city":"tokyo",
         "height":167
         },
         {"name":"muxialing",
         "age":32,
         "city":"ningbo",
         "height":170
         },
         {"name":"linana",
         "age":24,
         "city":"shanghai",
         "height":173
         }

    ]
}

#取出并打印所有女孩的信息

print(info.get('girls'))

#for 遍历打印所有女孩的信息
for i in info.get('girls'):
    #print(i)
    #打印出字典里每个女孩的名字
    print(i.get('name'))

    #打印出字典里每个女孩的城市
    print(i.get('city'))
    
    #打印出字典里每个女孩的身高
    print(i.get('height'))

    


