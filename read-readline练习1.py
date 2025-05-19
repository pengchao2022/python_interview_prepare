
with open('file.txt', 'r', encoding='utf-8') as fp:
     print(fp.read()) #读取文本的全部内容

     print(fp.readline()) #读取文本的一行

     print(fp.readlines()) #读取文本全部 包括空格

